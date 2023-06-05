# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.webkit.launch()
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     page.screenshot(path="example.png")
#     browser.close()

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False,slow_mo=50)
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="/Users/wevilaguo/Desktop/screenshotexample")
    browser.close()