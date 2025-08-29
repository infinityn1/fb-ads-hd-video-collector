import asyncio
import os
import json
from playwright.async_api import async_playwright

# Constant for Facebook Ads Library URL
FACEBOOK_ADS_LIBRARY_URL = "your_facebook_ads_library_url"

# Output file to store found HD video URLs
OUTPUT_FILE = "hd_video_urls.txt"

# Read previously saved URLs to avoid duplicates
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r") as f:
        saved_urls = set(line.strip() for line in f)
else:
    saved_urls = set()

found_count = 0

async def save_url(url: str):
    """Save HD video URL to file if not already saved"""
    global found_count
    if url in saved_urls:
        return
    with open(OUTPUT_FILE, "a") as f:
        f.write(url + "\n")
    saved_urls.add(url)
    found_count += 1

async def main():
    global found_count
    async with async_playwright() as p:
        # Launch Chromium using local Chrome
        browser = await p.chromium.launch(channel="chrome", headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        async def handle_response(response):
            if "graphql" in response.url and response.status == 200:
                try:
                    text = await response.text()
                    data = json.loads(text)

                    # Recursive search for HD video URLs in JSON
                    def find_hd_videos(obj):
                        urls = []
                        if isinstance(obj, dict):
                            for k, v in obj.items():
                                if k in ("video_hd_url", "playable_url_quality_hd") and isinstance(v, str):
                                    urls.append(v)
                                else:
                                    urls.extend(find_hd_videos(v))
                        elif isinstance(obj, list):
                            for item in obj:
                                urls.extend(find_hd_videos(item))
                        return urls

                    video_urls = find_hd_videos(data)
                    for url in video_urls:
                        await save_url(url)

                except json.JSONDecodeError:
                    print("[WARNING] Response is not valid JSON, skipping...")
                except Exception as e:
                    print(f"[ERROR parsing response] {e}")

        # Attach response handler
        page.on("response", handle_response)

        # Open Facebook Ads Library page using the constant URL
        await page.goto(FACEBOOK_ADS_LIBRARY_URL)

        print("Scroll the page manually in Chromium. Press Ctrl+C to stop.")

        try:
            while True:
                await asyncio.sleep(2)
                print(f"[STATUS] Total found URLs: {found_count}")
        except KeyboardInterrupt:
            print("\n[INFO] Script stopped by user.")
            print(f"[FINAL STATS] Total found URLs: {found_count}")

asyncio.run(main())
