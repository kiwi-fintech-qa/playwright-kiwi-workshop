from exercises.tasks.resources.resource_05 import KiwiPage


# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # 1. Open the kiwi.com website (wait for page to load) and accept cookies
    kiwi_page = KiwiPage(page)

    # 2. Clear the "from" location
    page.locator("").click()
    page.locator("").wait_for(state="")

    # 3. Type in "Vienna" to the "from" field
    page.locator("").fill("")

    # 4. Select the "Vienna, Austria" result from the dropdown
    page.locator("").click()

    # 5. Type in "Brno" to the "to" field
    page.locator("").fill("")

    # 6. Select the "Brno, Czechia" result from the dropdown
    page.locator("").fill("")

    # 7. Uncheck the "Booking" checkbox
    page.locator("").click()

    # 8. Hit the "Search" button
    page.locator("").click()

    # 9. Available connections should be displayed
    page.locator("").wait_for(timeout=10000)
    page.locator("").first.wait_for(state="")

    # (10. variation: among the results, this first one is cheaper than 10 000 CZK)
