# Facebook HD Video URL Collector

This Python script collects **HD video URLs** from the **Facebook Ads Library** and saves them into a `.txt` file.  
It **does not download videos**, only stores the links for later use. Duplicate URLs are automatically ignored.

---

## Features

- Collects HD video URLs (`video_hd_url` or `playable_url_quality_hd`) from Facebook Ads Library responses.
- Automatically avoids duplicate URLs.
- Outputs URLs to `hd_video_urls.txt`.
- Works in **real-time** as you scroll manually through the Ads Library page.
- Shows the total number of URLs found in the terminal.

---

## Why Use This Script?

- **Collect HD Video URLs Easily**: Automatically finds HD video links from Facebook Ads Library.  
- **No Downloads Needed**: Only saves URLs, saving bandwidth and storage.  
- **Duplicate-Free**: Prevents writing the same URL twice.  
- **Real-Time Updates**: Shows live counts as you scroll the page.  
- **Deep JSON Parsing**: Finds URLs even in nested GraphQL responses.  
- **Simple Setup**: Minimal dependencies and automatic Chromium management.  
- **Safe**: Only collects URLs, no spamming or downloading involved.  

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
