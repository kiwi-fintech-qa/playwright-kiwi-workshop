def open_kiwi_website(page):
    # 1. Open the kiwi.com website (https://www.kiwi.com/en/)
    page.goto("https://www.kiwi.com/en/")

    # 2. Accept cookies by clicking the appropriate button
    page.click("[data-test='CookiesPopup-Accept']")

    # 3. Assert the expected text is displayed
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")
