def open_kiwi_website_and_accept_cookies(page):
    page.goto("https://www.kiwi.com/en/")
    page.locator("[data-test='CookiesPopup-Accept']").click()
