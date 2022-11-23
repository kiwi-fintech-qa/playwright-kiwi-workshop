import math


# Filling out paid baggage options on Passenger details is reflected by the reservation bill
def test_filling_out_paid_baggage_options_on_passenger_details_is_reflected_by_the_reservation_bill(page):
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

    # 4. Fill out the Email, Phone, Given names, Surnames and the DD and YYYY fields of Date of birth as follows:
    # 4.1. Email: play@wrig.ht
    page.fill("[name=email]", "play@wrig.ht")

    # 4.2. Phone: 123123123
    page.fill("[name=phone]", "123123123")

    # 4.3. Given names: Play
    page.fill("[name=firstname]", "Play")

    # 4.4. Surnames: Wright
    page.fill("[name=lastname]", "Wright")

    # 4.5. DD: 1
    page.fill("[name=birthDay]", "1")

    # 4.6. YYYY: 1901
    page.fill("[name=birthYear]", "1901")

    # 5. In the following dropdowns select the following values:
    # 5.1. Nationality: United Kingdom
    page.select_option("[name=nationality]", value="gb")

    # 5.2. Gender: Female
    page.select_option("[name=title]", value="ms")

    # 5.3. Month: January
    page.select_option("[name=birthMonth]", value="01")

    # 6. In the Cabin or carry-on baggage section select the Carry-on bundle option and store its price value
    page.click("[data-test=Baggage-handBag] [data-test=Baggage-Option-1]")
    carry_on_baggage_price_with_currency_code = page.locator(
        "[data-test=Baggage-handBag] [data-test=Baggage-Option-1] [data-test=Baggage-OptionItem-Price]"
    ).inner_text()
    carry_on_baggage_price_value = float(carry_on_baggage_price_with_currency_code.split()[0])

    # 7. In the Checked baggage section select the 1× checked bag option and store its price value
    checked_baggage_price_value = None
    if page.is_hidden("[data-test=Baggage-EmptyOption]"):
        page.click("[data-test=Baggage-holdBag] [data-test=Baggage-Option-1]")
        checked_baggage_price_with_currency_code = page.locator(
            "[data-test=Baggage-holdBag] [data-test=Baggage-Option-1] [data-test=Baggage-OptionItem-Price]"
        ).inner_text()
        checked_baggage_price_value = float(checked_baggage_price_with_currency_code.split()[0])

    # 8. In the Travel insurance section select the No insurance option
    page.click("[data-test=ReservationPassengerInsurance-content] [type=none]")

    # 9. Hit the Continue button and verify the Ticker fare screen is displayed
    page.click("[data-test=StepControls-passengers-next]")
    page.wait_for_selector(
        "[aria-current=false] [class*=WizardStep__StyledLabel]:has-text('Passenger details')", state="visible"
    )
    page.wait_for_selector("[data-test=Breadcrumbs-step-PASSENGER] [aria-current=false]", state="visible")
    page.wait_for_selector("[data-test=Breadcrumbs-step-TICKET_FARE] [aria-current=step]", state="visible")

    # 10. Verify the following items are displayed in the reservation bill:
    # 10.1. Cabin baggage: value stored at step 6
    total_carry_on_baggage_price_with_currency_code = page.locator(
        "[data-test=bookingBillCabinBaggage] [class*=Price]"
    ).inner_text()
    total_carry_on_baggage_price_value = float(
        total_carry_on_baggage_price_with_currency_code.split()[0].replace(",", "")
    )
    assert carry_on_baggage_price_value == total_carry_on_baggage_price_value

    # 10.2. Checked baggage: value stored at step 7
    if checked_baggage_price_value:
        total_checked_baggage_price_with_currency_code = page.locator(
            "[data-test=bookingBillCheckedBaggage] [class*=Price]"
        ).inner_text()
        total_checked_baggage_price_value = float(
            total_checked_baggage_price_with_currency_code.split()[0].replace(",", "")
        )
        assert checked_baggage_price_value == total_checked_baggage_price_value

    # (11. variation: verify the total price corresponds with the sum of all items in the reservation bill)
    total_passenger_price_with_currency_code = page.locator(
        "[data-test=ReservationBill-item-passenger] [class*=Price]"
    ).inner_text()
    total_passenger_price_value = float(total_passenger_price_with_currency_code.split()[0].replace(",", ""))

    total_price_with_currency_code = page.locator("[class*=ReservationBillTotal] [class*=Price]").inner_text()
    total_price_value = float(total_price_with_currency_code.split()[0].replace(",", ""))

    total_of_items = (
        total_carry_on_baggage_price_value + total_checked_baggage_price_value + total_passenger_price_value
    )

    # Proper comparison of floats has to be used here:
    # https://docs.python.org/3/library/math.html#math.isclose
    # The basic assertion `assert total_of_items == total_price_value` would fail because of the way floats are stored.
    # Instead, we can check the absolute difference between the two values is very low, e.g., a bit over 0.01 CZK.

    # Also we can check how relatively distinct the values are:
    # With rel_tol=0.05 the values have to be 5% similar.
    # Here we decided arbitrarily that the values should have rel_tol=0.000000778, i.e., to be 0.00000778% similar.
    assert math.isclose(total_of_items, total_price_value, rel_tol=0.000000778, abs_tol=0.01000000000022)
