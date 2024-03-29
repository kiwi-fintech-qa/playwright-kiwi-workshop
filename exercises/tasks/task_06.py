from exercises.tasks.resources.resource_06 import KiwiPage


# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # Fill in the correct locator-methods where they are missing!
    # 1. Open the kiwi.com website and accept cookies
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website_and_accept_cookies()

    # 2. Clear the "from" location
    page.locator("")
    page.locator("").wait_for(state="")

    # 3. Type in "Vienna" to the "from" field
    page.locator("").fill("")

    # 4. Select the "Vienna, Austria" result from the dropdown
    page.locator("")

    # 5. Type in "Brno" to the "to" field
    page.locator("")

    # 6. Select the "Brno, Czechia" result from the dropdown
    page.locator("")

    # 7. Uncheck the "Booking" checkbox by clicking it
    page.locator("").first

    # 8. Click the "Search" button
    page.locator("")

    # 9. Available connections should be displayed
    page.locator("").wait_for(timeout=10000)
    page.locator("").first.wait_for(state="")

    # (10. variation: among the results, verify that the first one is cheaper than 10 000 CZK)
