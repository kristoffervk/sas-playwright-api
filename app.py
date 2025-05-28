from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_reese84():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.sas.no", timeout=60000)
        time.sleep(7)  # Wait for JS to generate the cookie

        cookies = context.cookies()
        browser.close()

        # Find the reese84 cookie
        for cookie in cookies:
            if cookie["name"] == "reese84":
                return jsonify(cookie)

        return jsonify({"error": "reese84 cookie not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
