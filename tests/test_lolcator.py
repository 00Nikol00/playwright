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
        nadpis_text=page.locator('text="Nadpis 1"')
        div_1 = page.locator('.container')
        div_2 = page.locator('.container-2')
        odkaz = page.locator('text="Odkaz"')
        odkaz_2 = page.locator('a[href="https://www.w3schools.com/"]')
        expect(nadpis_1).to_be_visible()
        expect(nadpis_text).to_be_visible()
        expect(div_1).to_be_visible()
        expect(div_2).to_be_visible()
        expect(nadpis_text).to_have_count(1)
        odkaz_2.click()
        expect(page).to_have_url("https://www.w3schools.com/")
        expect(odkaz).to_have_text("Odkaz")
        
        
        browser.close()