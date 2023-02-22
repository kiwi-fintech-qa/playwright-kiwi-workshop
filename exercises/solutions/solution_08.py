from exercises.solutions.resources.resource_06_12 import KiwiPage, SearchResultPage, PassengerDetailsPage


# Not filling out the required fields on Passenger details doesn't allow to proceed to the Ticket fare screen
def test_not_filling_out_required_fields_on_passenger_details_prevents_proceeding_to_ticket_fare_screen(page):
    # 1. Search for connections between any two cities, steps 1.1.-1.9. from task 6

    # Consider if the whole interaction with the initial search (steps 1.2.-1.8.) could be condensed into a single
    # method within the KiwiPage class!

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

    # 2. Hit the "Select" button of the first result
    search_result_page.hit_select_button_of_first_result()

    # 3. In the "Want to sign in first?" modal hit the "Continue as a guest" link
    search_result_page.hit_continue_as_guest_link()

    # 4. In the "Cabin or carry-on" baggage section select the 1× personal item option
    passenger_details_page = PassengerDetailsPage(page)
    passenger_details_page.select_cabin_baggage_single_item()

    # 5. If visible, in the "Checked baggage" section select the "No checked baggage" checkbox
    if passenger_details_page.baggage_empty_option.is_hidden():
        passenger_details_page.select_no_checked_baggage_checkbox()

    # 6. In the "Travel insurance" section select the "No insurance" option
    passenger_details_page.select_no_insurance()

    # 7. Hit the "Continue" button and verify that under the following fields the following errors are displayed:
    passenger_details_page.hit_continue_button_and_expect_to_stay_on_passenger_details_due_to_error()

    # 7.1. Email: Required for your tickets
    passenger_details_page.wait_for_email_error_to_be_displayed()

    # 7.2. Phone: Required field
    passenger_details_page.phone_field_error_should_be_displayed()

    # 7.3. Given names: Required field
    passenger_details_page.first_name_error_should_be_displayed()

    # 7.4. Surnames: Required field
    passenger_details_page.last_name_error_should_be_displayed()

    # 7.5. Nationality: Required field
    passenger_details_page.nationality_error_should_be_displayed()

    # 7.6. Gender: Required field
    passenger_details_page.gender_error_should_be_displayed()

    # 7.7. Date of birth: Required field
    passenger_details_page.birthdate_error_should_be_displayed()

    # (8. variation: fill out "Email" and "Phone", hit "Continue", and expect Required field error to be displayed
    # under the "Primary passenger" fields)
    # 8.1. Email: play@wrig.ht
    passenger_details_page.fill_out_passenger_email(email="play@wrig.ht")

    # 8.2. Phone: 123123123
    passenger_details_page.fill_out_passenger_phone(phone="123123123")

    # 8.3. Hit the "Continue" button and verify that under the following fields the following errors are displayed:
    passenger_details_page.hit_continue_button_and_expect_to_stay_on_passenger_details_due_to_error()

    # 8.4. Email: No error message
    passenger_details_page.wait_for_email_error_to_not_be_displayed()

    # 8.5. Phone: No error message
    passenger_details_page.phone_field_error_should_not_be_displayed()

    # 8.6. Given names: Required field
    passenger_details_page.first_name_error_should_be_displayed()

    # 8.7. Surnames: Required field
    passenger_details_page.last_name_error_should_be_displayed()

    # 8.8. Nationality: Required field
    passenger_details_page.nationality_error_should_be_displayed()

    # 8.9. Gender: Required field
    passenger_details_page.gender_error_should_be_displayed()

    # 8.10. Date of birth: Required field
    passenger_details_page.birthdate_error_should_be_displayed()

    # (9. variation: fill out and select the "Primary passenger" fields, clear the "Contact details" fields,
    # hit "Continue", and expect "Required for your tickets" error under the "Email" field and "Required"
    # field error under the "Phone" field)
    # 9.1. Email: empty
    passenger_details_page.fill_out_passenger_email(email="")

    # 9.2. Phone: empty
    passenger_details_page.fill_out_passenger_phone(phone="")

    # 9.3. Given names: Play
    passenger_details_page.fill_out_passenger_firstname(firstname="Play")

    # 9.4. Surnames: Wright
    passenger_details_page.fill_out_passenger_lastname(lastname="Wright")

    # 9.5. DD: 1
    passenger_details_page.fill_out_passenger_birthday(birthday="1")

    # 9.6. YYYY: 1901
    passenger_details_page.fill_out_passenger_birthyear(birthyear="1901")

    # 9.7. Nationality: United Kingdom
    passenger_details_page.select_passenger_nationality(nationality="gb")

    # 9.8. Gender: Female
    passenger_details_page.select_passenger_title(title="ms")

    # 9.9. Month: January
    passenger_details_page.select_passenger_birthmonth(birthmonth="01")

    # 9.10. Hit the "Continue" button and verify that under the following fields the following errors are displayed:
    passenger_details_page.hit_continue_button_and_expect_to_stay_on_passenger_details_due_to_error()

    # 9.11. Email: Required for your tickets
    passenger_details_page.wait_for_email_error_to_be_displayed()

    # 9.12. Phone: Required field
    passenger_details_page.phone_field_error_should_be_displayed()

    # 9.13. Given names: No error
    passenger_details_page.first_name_error_should_not_be_displayed()

    # 9.14. Surnames: No error
    passenger_details_page.last_name_error_should_not_be_displayed()

    # 9.15. Nationality: No error
    passenger_details_page.nationality_error_should_not_be_displayed()

    # 9.16. Gender: No error
    passenger_details_page.gender_error_should_not_be_displayed()

    # 9.17. Date of birth: No error
    passenger_details_page.birthdate_error_should_not_be_displayed()
