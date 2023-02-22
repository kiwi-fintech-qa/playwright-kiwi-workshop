from exercises.solutions.resources.resource_06_12 import KiwiPage, SearchResultPage


# Searching with additional transportation options shows results cheaper than 3 000 CZK
def test_searching_with_additional_transportation_options_shows_results_cheaper_than_3k_czk(page):
    # 1. Steps 1.1.-1.9. from the previous scenario, but using class methods instead
    # 1.1. Open the kiwi.com website and accept cookies
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website_and_accept_cookies()

    # 1.2. Clear the "from" location
    kiwi_page.clear_the_from_field()

    # 1.3. Type in "Vienna" to the "from" field
    kiwi_page.type_origin_location_into_input_field(location="Vienna")

    # 1.4. Select the "Vienna, Austria" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Vienna, Austria")

    # 1.5. Type in "Brno" to the "to" field
    kiwi_page.type_destination_location_into_input_field(location="Brno")

    # 1.6. Select the "Brno, Czechia" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Brno, Czechia")

    # 1.7. Uncheck the "Booking" checkbox
    kiwi_page.uncheck_booking_checkbox()

    # 1.8. Hit the "Search" button
    kiwi_page.hit_search_button()

    # 1.9. Available connections should be displayed
    search_result_page = SearchResultPage(page)

    # 2. Check the "Bus" checkbox in the "Transport" left-hand section of the results
    search_result_page.check_a_transport_option_checkbox(option="Bus")

    # 3. Verify the first result is cheaper than 3 000 CZK
    first_result_with_currency_code = search_result_page.first_result_card.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 3000

    # (4. variation: on step 2. check the "Train" checkbox in the "Transport" left-hand section as well;
    # on step 3. verify the results are cheaper than 1 000 CZK)

    # 4.1 Check the "Train" checkbox in the "Transport" left-hand section as well
    search_result_page.check_a_transport_option_checkbox(option="Train")

    # 4.2 Verify the results are cheaper than 1 000 CZK
    first_result_with_currency_code = search_result_page.first_result_card.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 1000
