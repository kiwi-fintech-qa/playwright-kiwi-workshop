from exercises.solutions.resources.resource_07_12 import KiwiPage, SearchResultPage


# Sorting panel actions can be used for sorting the search results
# TODO: run without any --slowmo (slow execution leads to some weird loading on steps 2 and 3; or fix it)
def test_sorting_panel_actions_can_be_used_for_sorting_the_search_results(page):
    # 1. Steps 1.1.-1.9. from the previous task
    # 1.1. Open the kiwi.com website and accept cookies
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website_and_accept_cookies()

    # 1.2. Clear the "from" location
    kiwi_page.clear_the_from_field()

    # 1.3. Type in "Brno" to the "from" field
    kiwi_page.type_origin_location_into_input_field(location="Brno")

    # 1.4. Select the "Brno, Czechia" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Brno, Czechia")

    # 1.5. Type in "Vienna" to the "to" field
    kiwi_page.type_destination_location_into_input_field(location="Vienna")

    # 1.6. Select the "Vienna, Austria" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Vienna, Austria")

    # 1.7. Uncheck the "Booking" checkbox
    kiwi_page.uncheck_booking_checkbox()

    # 1.8. Hit the "Search" button
    kiwi_page.hit_search_button()

    # 1.9. Available connections should be displayed
    search_result_page = SearchResultPage(page)

    # 2. Check the "Train" checkbox in the "Transport" left-hand section of the results
    search_result_page.check_a_transport_option_checkbox(option="Train")

    # 3. Select the "Cheapest" sorting option from the sorting panel
    search_result_page.sort_results_by_price()

    # 4. Store the price value of the first few (e.g., 3) results into a (Python) list
    result_values_list = []
    for i in range(3):
        nth_result_with_currency_code = (
            page.locator(
                "[data-test=ResultCardPrice][class*=ResultCardstyled__PriceText]"
            )
            .nth(i)
            .inner_text()
            .split()[0]
        )
        nth_result_value = int(nth_result_with_currency_code.replace(",", ""))
        result_values_list.append(nth_result_value)

    # 5. Verify the first result is either the cheapest of the stored values, or the same as the rest of them
    assert result_values_list[0] <= result_values_list[1]

    # (6. variation: on step 3. select the "Fastest" sorting option; on step 5. identify the cheapest of the stored
    # results [i.e., identify the cheapest of the several fastest connections)
    # 6.1. Select the "Fastest" sorting option
    search_result_page.sort_results_by_duration()

    # 6.2. Identify the cheapest of the several fastest connections
    result_values_list = []
    for i in range(3):
        nth_result_with_currency_code = (
            page.locator(
                "[data-test=ResultCardPrice][class*=ResultCardstyled__PriceText]"
            )
            .nth(i)
            .inner_text()
            .split()[0]
        )
        nth_result_value = int(nth_result_with_currency_code.replace(",", ""))
        result_values_list.append(nth_result_value)

    print(
        f"The cheapest of the several fastest connections costs {min(result_values_list)} CZK"
    )
