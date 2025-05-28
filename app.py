from playwright.sync_api import sync_playwright
import time
import json

def get_reese_cookie():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            viewport={'width': 1280, 'height': 800}
        )
        page = context.new_page()

        # Set additional headers
        page.set_extra_http_headers({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'upgrade-insecure-requests': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        })

        # Go to site and wait for scripts to run
        page.goto("https://www.sas.no", wait_until="load", timeout=60000)
        time.sleep(10)  # wait for JS like reese84 generator to run

        # Optionally scroll a bit to simulate real user
        page.mouse.wheel(0, 500)
        time.sleep(1)

        # Get cookies
        cookies = context.cookies()
        for cookie in cookies:
            if 'reese84' in cookie['name']:
                print("Found reese84 cookie:")
                print(json.dumps(cookie, indent=2))
                break
        else:
            print("No reese84 cookie found.")

        browser.close()

if __name__ == "__main__":
    get_reese_cookie()
