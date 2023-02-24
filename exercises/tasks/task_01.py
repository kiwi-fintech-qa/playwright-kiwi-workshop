# Navigate to the Kiwi.com website
# Verify the "Book cheap flights other sites simply can’t find." text is displayed.
def test_navigate_to_kiwi(page):
    # 1. Open the kiwi.com website (https://www.kiwi.com/en/)
    page.goto("")

    # 2. Accept cookies by clicking the appropriate button
    page.locator("").click()

    # 3. Assert that the expected text is displayed
    assert page.locator("text=").is_visible()

    # 4 Hit the "Explore" button!
    page.locator("").click()
