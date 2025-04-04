from playwright.sync_api import sync_playwright, expect
import os
import urllib.parse

def test_page_title():
    cesta = os.path.abspath("./src/index.html")
    cesta = urllib.parse.unquote(cesta)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{cesta}")
        nadpis_1 = page.locator('h1').first
        expect(nadpis_1).to_be_visible()

        browser.close()