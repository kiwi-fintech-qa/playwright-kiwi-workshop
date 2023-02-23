class KiwiPage:
    def __init__(self, page):
        self.page = page
        self.cookies_popup_button_accept = page.locator("[data-test='CookiesPopup-Accept']")
        self.kiwi_page_subtitle = page.locator("text=Book cheap flights other sites simply can’t find.")

    def open_kiwi_website_and_accept_cookies(self):
        self.page.goto("https://www.kiwi.com/en/")
        self.cookies_popup_button_accept.click()
        assert self.kiwi_page_subtitle.is_visible()
