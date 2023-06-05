from playwright.sync_api import sync_playwright
with sync_playwright() as playwight:
    browser=playwight.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://azure.microsoft.com')
