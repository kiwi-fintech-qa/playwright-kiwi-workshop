from exercises.solutions.resources.resource_06_12 import KiwiPage, SearchResultPage, PassengerDetailsPage


# Localized currency is retained in Passenger details
def test_localized_currency_is_retained_in_passenger_details(page):
    # 1. Hit the 🇬🇧 CZK button in the navigation bar at the top of the search page
    # 1.1. Open the kiwi.com website (wait for page to load)
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website()

    # 1.2 Open the localization settings and wait for the localization modal to be displayed
    kiwi_page.open_regional_settings()

    # 2. Set the currency in the Language and currency modal to EUR
    currency_code = "EUR"
    kiwi_page.set_currency(currency_code)

    # 3. Hit the Save & continue button
    kiwi_page.save_regional_settings()

    # 4. Search for connections between any two cities (while un-checking the Booking.com checkbox, as in previous scenarios)
    # 4.1. Clear the "from" location (here with a stabilization to ensure the place-chip is always removed)
    kiwi_page.clear_the_from_field(stabilized=True)

    # 4.2. Type in "Brno" to the "from" field
    kiwi_page.type_origin_location_into_input_field(location="Brno")

    # 4.3. Select the "Brno, Czechia" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Brno, Czechia")

    # 4.4. Type in "Vienna" to the "to" field
    kiwi_page.type_destination_location_into_input_field(location="Vienna")

    # 4.5. Select the "Vienna, Austria" result from the dropdown
    kiwi_page.select_location_from_dropdown(location="Vienna, Austria")

    # 4.6. Uncheck the "Booking" checkbox
    kiwi_page.uncheck_booking_checkbox()

    # 4.7. Hit the "Search" button
    kiwi_page.hit_search_button()

    # 4.8. Available connections should be displayed
    search_result_page = SearchResultPage(page)
    search_result_page.wait_for_available_connections_to_be_displayed()

    # 5. Store the price value of the first result
    first_result_without_currency_code = search_result_page.first_result_card.inner_text().split()[0]
    first_result_value = int(first_result_without_currency_code)

    # 6. Hit the Select button of the first result
    search_result_page.hit_select_button_of_first_result()

    # 7. In the "Want to sign first?" modal hit the "Continue as a guest link"
    search_result_page.hit_continue_as_guest_link()

    # 8. Verify the Total (EUR) price value corresponds with the one stored on step 5.
    passenger_details_page = PassengerDetailsPage(page)
    total_price_with_currency_code = passenger_details_page.reservation_bill_total.inner_text()
    total_price_value = int(total_price_with_currency_code.split()[0])
    assert first_result_value == total_price_value

    # (9. variation: verify the currency code selected on step 1 is displayed next to Total in the reservation bill)
    total_currency_code = passenger_details_page.total_currency_label.inner_text().split("(")[1].strip(")")
    assert currency_code == total_currency_code
