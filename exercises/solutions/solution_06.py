# Not filling out the required fields on Passenger details doesn't allow to proceed to the Ticket fare screen
def test_not_filling_out_required_fields_on_passenger_details_prevents_proceeding_to_ticket_fare_screen(page):
    # 1. Search for connections between any two cities (while un-checking the Booking.com checkbox,
    # as in previous scenarios)
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
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 1.5. Type in `Bucharest` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Bucharest")

    # 1.6. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 1.7. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 1.8. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 1.9. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # 2. Hit the Select button of the first result
    page.click("[data-test=BookingButton]")
    page.wait_for_selector("[data-test=MagicLogin]", state="visible")

    # 3. In the Want to sign first? modal hit the Continue as a guest link
    page.click("[data-test=MagicLogin-GuestTextLink]")
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="hidden")
    page.wait_for_selector("[data-test=Reservation-content]", state="visible")
    page.wait_for_selector("[data-test=Breadcrumbs-step-PASSENGER] [aria-current=step]", state="visible")

    # 4. In the Cabin or carry-on baggage section select the 1× personal item option
    page.click("[data-test=Baggage-handBag] [data-test=Baggage-Option-0]")

    # 5. If visible, in the Checked baggage section select the No checked baggage checkbox
    if page.is_hidden("[data-test=Baggage-EmptyOption]"):
        page.click("[class*=Checkbox]:has([data-test=Baggage-NoBagsToCheckIn])")

    # 6. In the Travel insurance section select the No insurance option
    page.click("[data-test=ReservationPassengerInsurance-content] [type=none]")

    # 7. Hit the Continue button and verify that under the following fields the following errors are displayed:
    page.click("[data-test=StepControls-passengers-next]")

    # 7.1. Email: Required for your tickets
    page.wait_for_selector("[data-test=ContactEmail] [aria-live=polite]:has-text('Required for your tickets')", state="visible")

    # 7.2. Phone: Required field
    page.is_visible("[data-test=ContactPhone] [aria-live=polite]:has-text('Required field')")

    # 7.3. Given names: Required field
    page.is_visible("[data-test=ReservationPassenger-FirstName] [aria-live=polite]:has-text('Required field')")

    # 7.4. Surnames: Required field
    page.is_visible("[data-test=ReservationPassenger-LastName] [aria-live=polite]:has-text('Required field')")

    # 7.5. Nationality: Required field
    page.is_visible("[class*=Select]:has([name=nationality]) [aria-live=polite]:has-text('Required field')")

    # 7.6. Gender: Required field
    page.is_visible("[class*=Select]:has([name=title]) [aria-live=polite]:has-text('Required field')")

    # 7.7. Date of birth: Required field
    page.wait_for_selector("[class*=InputGroup]:has([name=birthDay]) [aria-live=polite]:has-text('Required field')")

    # (8. variation: fill out Email and Phone, hit Continue, and expect Required filed error to be displayed
    # under the Primary passenger fields)
    # 8.1. Email: play@wrig.ht
    page.fill("[name=email]", "play@wrig.ht")

    # 8.2. Phone: 123123123
    page.fill("[name=phone]", "123123123")

    # 8.3. Hit the Continue button and verify that under the following fields the following errors are displayed:
    page.click("[data-test=StepControls-passengers-next]")

    # 8.4. Email: No error message
    page.wait_for_selector("[data-test=ContactEmail] [aria-live=polite]:has-text('Required for your tickets')", state="hidden")

    # 8.5. Phone: No error message
    page.is_hidden("[data-test=ContactPhone] [aria-live=polite]:has-text('Required field')")

    # 8.6. Given names: Required field
    page.is_visible("[data-test=ReservationPassenger-FirstName] [aria-live=polite]:has-text('Required field')")

    # 8.7. Surnames: Required field
    page.is_visible("[data-test=ReservationPassenger-LastName] [aria-live=polite]:has-text('Required field')")

    # 8.8. Nationality: Required field
    page.is_visible("[class*=Select]:has([name=nationality]) [aria-live=polite]:has-text('Required field')")

    # 8.9. Gender: Required field
    page.is_visible("[class*=Select]:has([name=title]) [aria-live=polite]:has-text('Required field')")

    # 8.10. Date of birth: Required field
    page.is_visible("[class*=InputGroup]:has([name=birthDay]) [aria-live=polite]:has-text('Required field')")

    # (9. variation: fill out and select the Primary passenger fields, clear the Contact details fields, hit Continue,
    # and expect Required for your tickets error under the Email field and Required field error under the Phone field)
    # 9.1. Email: play@wrig.ht
    page.fill("[name=email]", "")

    # 9.2. Phone: 123123123
    page.fill("[name=phone]", "")

    # 9.3. Given names: Play
    page.fill("[name=firstname]", "Play")

    # 9.4. Surnames: Wright
    page.fill("[name=lastname]", "Wright")

    # 9.5. DD: 1
    page.fill("[name=birthDay]", "1")

    # 9.6. YYYY: 1901
    page.fill("[name=birthYear]", "1901")

    # 9.7. Nationality: United Kingdom
    page.select_option("[name=nationality]", value="gb")

    # 9.8. Gender: Female
    page.select_option("[name=title]", value="ms")

    # 9.9. Month: January
    page.select_option("[name=birthMonth]", value="01")

    # 9.10. Hit the Continue button and verify that under the following fields the following errors are displayed:
    page.click("[data-test=StepControls-passengers-next]")

    # 9.11. Email: Required for your tickets
    page.wait_for_selector("[data-test=ContactEmail] [aria-live=polite]:has-text('Required for your tickets')", state="visible")

    # 9.12. Phone: Required field
    page.is_visible("[data-test=ContactPhone] [aria-live=polite]:has-text('Required field')")

    # 9.13. Given names: No error
    page.is_hidden("[data-test=ReservationPassenger-FirstName] [aria-live=polite]:has-text('Required field')")

    # 9.14. Surnames: No error
    page.is_hidden("[data-test=ReservationPassenger-LastName] [aria-live=polite]:has-text('Required field')")

    # 9.15. Nationality: No error
    page.is_hidden("[class*=Select]:has([name=nationality]) [aria-live=polite]:has-text('Required field')")

    # 9.16. Gender: No error
    page.is_hidden("[class*=Select]:has([name=title]) [aria-live=polite]:has-text('Required field')")

    # 9.17. Date of birth: No error
    page.is_hidden("[class*=InputGroup]:has([name=birthDay]) [aria-live=polite]:has-text('Required field')")
