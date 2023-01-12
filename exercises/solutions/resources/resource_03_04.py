def open_kiwi_website(page):
    # 1. Open the kiwi.com website (https://www.kiwi.com/en/)
    page.goto("https://www.kiwi.com/en/")

    # 2. Accept cookies by clicking the appropriate button
    page.locator("[data-test='CookiesPopup-Accept']").click()

    # 3. Assert the expected text is displayed
    assert page.locator("text=Book cheap flights other sites simply can’t find.").is_visible()
