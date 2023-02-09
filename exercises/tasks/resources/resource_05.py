class KiwiPage:
    def __init__(self, page):
        self.page = page

        self.cookies_popup_button_accept = page.locator("")
        self.kiwi_page_subtitle = page.locator("")

    def open_kiwi_website_and_accept_cookies(self):
        self.page.goto("https://www.kiwi.com/en/")
        self.cookies_popup_button_accept.click()
