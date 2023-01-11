from exercises.solutions.resources.resource_06_12 import (
    KiwiPage,
    SearchResultPage,
    PassengerDetailsPage,
    TicketFarePage,
)
import math


# Filling out paid baggage options on Passenger details is reflected by the reservation bill
def test_filling_out_paid_baggage_options_on_passenger_details_is_reflected_by_the_reservation_bill(page):
    # 1. Search for connections between any two cities (while un-checking the Booking.com checkbox,
    # as in previous scenarios)
    # 1.1. Open the kiwi.com website (wait for page to load)
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website()

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
    search_result_page.wait_for_available_connections_to_be_displayed()

    # 2. Hit the Select button of the first result
    search_result_page.hit_select_button_of_first_result()

    # 3. In the "Want to sign first?" modal hit the "Continue as a guest link"
    search_result_page.hit_continue_as_guest_link()

    # 4. Fill out the Email, Phone, Given names, Surnames and the DD and YYYY fields of Date of birth as follows:
    # 4.1. Email: play@wrig.ht
    passenger_details_page = PassengerDetailsPage(page)
    passenger_details_page.fill_out_passenger_email(email="play@wrig.ht")

    # 4.2. Phone: 123123123
    passenger_details_page.fill_out_passenger_phone(phone="123123123")

    # 4.3. Given names: Play
    passenger_details_page.fill_out_passenger_firstname(firstname="Play")

    # 4.4. Surnames: Wright
    passenger_details_page.fill_out_passenger_lastname(lastname="Wright")

    # 4.5. DD: 1
    passenger_details_page.fill_out_passenger_birthday(birthday="1")

    # 4.6. YYYY: 1901
    passenger_details_page.fill_out_passenger_birthyear(birthyear="1901")

    # 5. In the following dropdowns select the following values:
    # 5.1. Nationality: United Kingdom
    passenger_details_page.select_passenger_nationality(nationality="gb")

    # 5.2. Gender: Female
    passenger_details_page.select_passenger_title(title="ms")

    # 5.3. Month: January
    passenger_details_page.select_passenger_birthmonth(birthmonth="01")

    # 6. In the Cabin or carry-on baggage section select the Carry-on bundle option and store its price value
    passenger_details_page.select_cabin_baggage_bundle()
    carry_on_baggage_price_value = passenger_details_page.get_carry_on_baggage_price_value()

    # 7. In the Checked baggage section select the 1× checked bag option and store its price value
    checked_baggage_price_value = 0
    if passenger_details_page.baggage_empty_option.is_hidden():
        passenger_details_page.select_checked_baggage_once()
        checked_baggage_price_value = passenger_details_page.get_checked_baggage_price_value()

    # 8. In the Travel insurance section select the No insurance option
    passenger_details_page.select_no_insurance()

    # 9. Hit the Continue button and verify the Ticker fare screen is displayed
    passenger_details_page.proceed_to_ticket_fare_page()

    # 10. Verify the following items are displayed in the reservation bill:
    # 10.1. Cabin baggage: value stored at step 6
    ticket_fare_page = TicketFarePage(page)
    total_carry_on_baggage_price_value = ticket_fare_page.get_carry_on_baggage_price_value()
    assert carry_on_baggage_price_value == total_carry_on_baggage_price_value

    # 10.2. Checked baggage: value stored at step 7
    total_checked_baggage_price_value = 0
    if checked_baggage_price_value:
        total_checked_baggage_price_value = ticket_fare_page.get_checked_baggage_price_value()
        assert checked_baggage_price_value == total_checked_baggage_price_value

    # (11. variation: verify the total price corresponds with the sum of all items in the reservation bill)
    total_passenger_price_value = ticket_fare_page.get_passenger_price_value()
    total_price_value = ticket_fare_page.get_total_price_value()
    total_of_items = (
        total_carry_on_baggage_price_value + total_checked_baggage_price_value + total_passenger_price_value
    )

    # Proper comparison of floats has to be used here:
    # https://docs.python.org/3/library/math.html#math.isclose
    # The basic assertion "assert total_of_items == total_price_value" would fail because of the way floats are stored.
    # Instead, we can check the absolute difference between the two values is very low, e.g., a bit over 0.01 CZK.

    # Also we can check how relatively distinct the values are:
    # With rel_tol=0.05 the values have to be 5% similar.
    # Here we decided arbitrarily that the values should have rel_tol=0.000000778, i.e., to be 0.00000778% similar.
    assert math.isclose(total_of_items, total_price_value, rel_tol=0.000000778, abs_tol=0.01000000000022)
