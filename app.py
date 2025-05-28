from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def get_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.sas.no", timeout=60000)
        page.wait_for_timeout(7000)
        cookies = context.cookies()
        browser.close()
        return jsonify({cookie["name"]: cookie["value"] for cookie in cookies})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
