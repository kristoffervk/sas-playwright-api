from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

@app.route("/")
def get_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            locale="nb-NO"
        )
        page = context.new_page()

        # Set extra headers manually
        page.set_extra_http_headers({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        })

        page.goto("https://www.sas.no", wait_until="networkidle", timeout=90000)

        # Wait extra to let JS load & set cookies like reese84
        time.sleep(8)

        cookies = context.cookies()
        browser.close()
        return jsonify(cookies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
