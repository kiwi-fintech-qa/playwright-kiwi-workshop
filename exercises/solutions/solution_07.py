# Sorting panel actions can be used for sorting the search results
# TODO: run without any --slowmo (slow execution leads to some weird loading on steps 2 and 3; or fix it)
def test_sorting_panel_actions_can_be_used_for_sorting_the_search_results(page):
    # 1. Steps 1-9. from the Searching for a connection displays results scenario, but with the From location
    # set to Brno and the To location set to Bucharest
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Clear the `from` location
    page.click("[data-test=PlacePickerInputPlace-close]")
    page.wait_for_selector("[data-test=PlacePickerInputPlace-close]", state="hidden")

    # 1.3. Type in `Brno` to the `from` field
    page.fill("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]", "Brno")

    # 1.4. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]:has-text('Brno, Czechia')")

    # 1.5. Type in `Bucharest` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Bucharest")

    # 1.6. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]:has-text('Bucharest, Romania')")

    # 1.7. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 1.8. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 1.9. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # 2. Check the Train checkbox in the Transport left-hand section of the results
    page.click("[class*=FilterWrapper]:has([data-test=TransportOptionCheckbox-train])")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="visible")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="hidden")

    # 3. Select the Cheapest sorting option from the sorting panel
    page.click("[data-test=SortBy-price]")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="visible")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="hidden")

    # 4. Store the price value of the first few (e.g., 5) results into a (Python) list
    result_values_list = []
    for i in range(5):
        nth_result_with_currency_code = (
            page.locator("[data-test=ResultCardPrice][class*=ResultCardstyled__PriceText]")
            .nth(i)
            .inner_text()
            .split()[0]
        )
        nth_result_value = int(nth_result_with_currency_code.replace(",", ""))
        result_values_list.append(nth_result_value)

    # 5. Verify the first result is either the cheapest of the stored values, or the same as the rest of them
    assert result_values_list[0] <= result_values_list[1]

    # (6. variation: on step 3. select the Fastest sorting option; on step 5. identify the cheapest of the stored
    # results [i.e., identify the cheapest of the several fastest connections)
    # 6.1. Select the Fastest sorting option
    page.click("[data-test=SortBy-duration]")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="visible")
    page.wait_for_selector("[data-test=ResultList] [class*=LoadingProvidersstyled]", state="hidden")

    # 6.2. Identify the cheapest of the several fastest connections
    result_values_list = []
    for i in range(5):
        nth_result_with_currency_code = (
            page.locator("[data-test=ResultCardPrice][class*=ResultCardstyled__PriceText]")
            .nth(i)
            .inner_text()
            .split()[0]
        )
        nth_result_value = int(nth_result_with_currency_code.replace(",", ""))
        result_values_list.append(nth_result_value)

    print(f"The cheapest of the several fastest connections costs {min(result_values_list)} CZK")
