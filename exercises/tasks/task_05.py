from exercises.tasks.resources.resource_05 import KiwiPage


# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # 1. Open the kiwi.com website (wait for page to load)
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website()

    # 2. Clear the "from" location
    page.click("")
    page.wait_for_selector("", state="")

    # 3. Type in "Vienna" to the "from" field
    page.fill("", "")

    # 4. Select the "Vienna, Austria" result from the dropdown
    page.click("")

    # 5. Type in "Brno" to the "to" field
    page.fill("", "")

    # 6. Select the "Brno, Czechia" result from the dropdown
    page.click("")

    # 7. Uncheck the "Booking" checkbox
    page.click("")

    # 8. Hit the "Search" button
    page.click("")

    # 9. Available connections should be displayed
    page.wait_for_selector("", timeout=10000)
    page.wait_for_selector("", state="")

    # (10. variation: among the results, this first one is cheaper than 10 000 CZK)
