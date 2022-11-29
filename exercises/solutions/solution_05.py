# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # 1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 2. Clear the `from` location
    page.click("[data-test=PlacePickerInputPlace-close]")
    page.wait_for_selector("[data-test=PlacePickerInputPlace-close]", state="hidden")

    # 3. Type in `Vienna` to the `from` field
    page.fill("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]", "Vienna")

    # 4. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]:has-text('Vienna, Austria')")

    # 5. Type in `Brno` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Brno")

    # 6. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 7. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 8. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 9. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # (10. variation: among the results, this first one is cheaper than 10 000 CZK)
    first_result_with_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 10000
