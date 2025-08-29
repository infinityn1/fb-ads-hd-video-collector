# Facebook HD Video URL Collector

This Python script collects **HD video URLs** from the **Facebook Ads Library** and saves them into a `.txt` file.  
It **does not download videos**, only stores the links for later use. Duplicate URLs are automatically ignored.

---

## Features

- Collects HD video URLs (`video_hd_url` or `playable_url_quality_hd`) from Facebook Ads Library responses.
- Automatically avoids duplicate URLs.
- Saves URLs to `hd_video_urls.txt`.
- Works in **real-time** as you scroll manually through the Ads Library page.
- Shows the total number of URLs found in the terminal.

---

## Why Use This Script?

- **Easy HD Video URL Collection**: Automatically finds HD video links from Facebook Ads Library.  
- **No Downloads**: Only saves URLs, reducing bandwidth and storage usage.  
- **Duplicate-Free**: Prevents writing the same URL twice.  
- **Live Updates**: Displays total found URLs in real-time while scrolling.  
- **Deep JSON Parsing**: Finds URLs even in nested GraphQL responses.  
- **Minimal Setup**: Simple Python script with Playwright managing Chromium.  
- **Safe**: Only collects URLs, no downloading or spamming is performed.

---

## How It Works

1. Run the Python script.  
2. A Chromium browser window opens and loads the Facebook Ads Library page.  
3. Scroll manually through the page. The script listens for GraphQL responses.  
4. Any HD video URLs found in the responses are saved into `hd_video_urls.txt`.  
5. Terminal shows live status of total URLs found.

---

## Requirements

- Python 3.10+  
- [Playwright](https://playwright.dev/python/)  
- Chromium or Chrome browser (Playwright will manage installation)

---

## Installation

1. Install required packages:

```bash
pip install playwright asyncio
