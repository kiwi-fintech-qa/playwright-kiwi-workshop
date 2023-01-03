# Open the kiwi.com website
def open_kiwi_website(page):
    # 1. Open the kiwi.com website (https://www.kiwi.com/en/)
    page.goto("")

    # 2. Accept cookies by clicking the appropriate button
    page.click("")

    # 3. Assert the expected text is displayed
    assert page.is_visible("text=")
