from exercises.solutions.resources.resource_05 import KiwiPage


# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # 1. Open the kiwi.com website (wait for page to load)
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website()

    # 2. Clear the "from" location
    page.locator("[data-test=PlacePickerInputPlace-close]").click()
    page.locator("[data-test=PlacePickerInputPlace-close]").wait_for(state="hidden")

    # 3. Type in "Vienna" to the "from" field
    page.locator("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]").fill("Vienna")

    # 4. Select the "Vienna, Austria" result from the dropdown
    page.locator("[data-test=PlacePickerRow-wrapper]:has-text('Vienna, Austria')").click()

    # 5. Type in "Brno" to the "to" field
    page.locator("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]").fill("Brno")

    # 6. Select the "Brno, Czechia" result from the dropdown
    page.locator("[data-test=PlacePickerRow-wrapper]:has-text('Brno, Czechia')").click()

    # 7. Uncheck the "Booking" checkbox
    page.locator("[class*=BookingcomSwitchstyled] [class*=Checkbox]").first.click()

    # 8. Hit the "Search" button
    page.locator("[data-test=LandingSearchButton]").click()

    # 9. Available connections should be displayed
    page.locator("[class*=ResultListstyled__ResultListWrapper]").wait_for(timeout=10000)
    page.locator("[data-test=ResultCardWrapper]").first.wait_for(state="visible")

    # (10. variation: among the results, this first one is cheaper than 10 000 CZK)
    first_result_with_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 10000
