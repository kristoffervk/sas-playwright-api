from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

@app.route("/")
def get_all_cookies():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                viewport={'width': 1280, 'height': 800}
            )
            page = context.new_page()

            # Set headers
            page.set_extra_http_headers({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'upgrade-insecure-requests': '1',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document'
            })

            # Visit page
            page.goto("https://www.sas.no", wait_until="load", timeout=60000)
            time.sleep(10)
            page.mouse.wheel(0, 500)
            time.sleep(1)

            # Return all cookies
            cookies = context.cookies()
            return jsonify({"cookies": cookies})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
