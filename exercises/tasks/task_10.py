from exercises.tasks.resources.resource_06_12 import KiwiPage, SearchResultPage

# Not filling out the required fields on Passenger details doesn't allow to proceed to the Ticket fare screen
def test_not_filling_out_required_fields_on_passenger_details_prevents_proceeding_to_ticket_fare_screen(page):
    # 1. Search for connections between any two cities (while un-checking the Booking.com checkbox,
    # as in previous scenarios)
    # 1.1. Open the kiwi.com website (wait for page to load)
    pass

    # 1.2. Clear the "from" location

    # 1.3. Type in "Brno" to the "from" field

    # 1.4. Select the 1st result from the dropdown

    # 1.5. Type in "Vienna" to the "to" field

    # 1.6. Select the 1st result from the dropdown

    # 1.7. Uncheck the "Booking" checkbox

    # 1.8. Hit the "Search" button

    # 1.9. Available connections should be displayed

    # 2. Hit the Select button of the first result

    # 3. In the Want to sign first? modal hit the Continue as a guest link

    # 4. In the Cabin or carry-on baggage section select the 1× personal item option

    # 5. If visible, in the Checked baggage section select the No checked baggage checkbox

    # 6. In the Travel insurance section select the No insurance option

    # 7. Hit the Continue button and verify that under the following fields the following errors are displayed:

    # 7.1. Email: Required for your tickets

    # 7.2. Phone: Required field

    # 7.3. Given names: Required field

    # 7.4. Surnames: Required field

    # 7.5. Nationality: Required field

    # 7.6. Gender: Required field

    # 7.7. Date of birth: Required field

    # (8. variation: fill out Email and Phone, hit Continue, and expect Required filed error to be displayed
    # under the Primary passenger fields)
    # 8.1. Email: play@wrig.ht

    # 8.2. Phone: 123123123

    # 8.3. Hit the Continue button and verify that under the following fields the following errors are displayed:

    # 8.4. Email: No error message

    # 8.5. Phone: No error message

    # 8.6. Given names: Required field

    # 8.7. Surnames: Required field

    # 8.8. Nationality: Required field

    # 8.9. Gender: Required field

    # 8.10. Date of birth: Required field

    # (9. variation: fill out and select the Primary passenger fields, clear the Contact details fields, hit Continue,
    # and expect Required for your tickets error under the Email field and Required field error under the Phone field)
    # 9.1. Email: empty

    # 9.2. Phone: empty

    # 9.3. Given names: Play

    # 9.4. Surnames: Wright

    # 9.5. DD: 1

    # 9.6. YYYY: 1901

    # 9.7. Nationality: United Kingdom

    # 9.8. Gender: Female

    # 9.9. Month: January

    # 9.10. Hit the Continue button and verify that under the following fields the following errors are displayed:

    # 9.11. Email: Required for your tickets

    # 9.12. Phone: Required field

    # 9.13. Given names: No error

    # 9.14. Surnames: No error

    # 9.15. Nationality: No error

    # 9.16. Gender: No error

    # 9.17. Date of birth: No error
