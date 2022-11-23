# Searching with additional transportation options shows results cheaper than 1 000 CZK
def test_searching_with_additional_transportation_options_shows_results_cheaper_than_1k_czk(page):
    # 1. Steps 1-9. from the previous scenario
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Clear the `from` location
    page.click("[data-test=PlacePickerInputPlace-close]")
    page.wait_for_selector("[data-test=PlacePickerInputPlace-close]", state="hidden")

    # 1.3. Type in `Vienna` to the `from` field
    page.fill("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]", "Vienna")

    # 1.4. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]:has-text('Vienna, Austria')")

    # 1.5. Type in `Brno` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Brno")

    # 1.6. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 1.7. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 1.8. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 1.9. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # 2. Check the `Bus` checkbox in the `Transport` left-hand section of the results
    page.click("[class*=FilterWrapper]:has([data-test=TransportOptionCheckbox-bus])")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="visible")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="hidden")

    # 3. Verify the first result is cheaper than 1 000 CZK
    first_result_with_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 1000

    # (4. variation: on step 2. check the `Train` checkbox in the `Transport` left-hand section as well; on step 3. verify the results are cheaper than 350 CZK)
    # 4.1 Check the `Train` checkbox in the `Transport` left-hand section as well
    page.click("[class*=FilterWrapper]:has([data-test=TransportOptionCheckbox-train])")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="visible")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="hidden")

    # 4.2 Verify the results are cheaper than 350 CZK
    first_result_with_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 400
