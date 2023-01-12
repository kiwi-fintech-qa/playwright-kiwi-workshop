class KiwiPage:
    def __init__(self, page):
        self.page = page

        self.cookies_popup_button_accept = page.locator("[data-test='CookiesPopup-Accept']")
        self.kiwi_page_subtitle = page.locator("text=Book cheap flights other sites simply can’t find.")

    def open_kiwi_website(self):
        # 1. Open the kiwi.com website (https://www.kiwi.com/en/)
        self.page.goto("https://www.kiwi.com/en/")

        # 2. Accept cookies by clicking the appropriate button
        self.cookies_popup_button_accept.click()

        # 3. Assert the expected text is displayed
        assert self.kiwi_page_subtitle.is_visible()
