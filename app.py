from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def get_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sas.no", timeout=60000)
        page.wait_for_timeout(7000)
        cookies = page.context.cookies()
        browser.close()
    return jsonify({cookie['name']: cookie['value'] for cookie in cookies})
