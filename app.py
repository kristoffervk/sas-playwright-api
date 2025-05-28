from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def get_cookie():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.sas.no", timeout=60000)
        cookies = context.cookies()
        browser.close()
        return jsonify(cookies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
