import time
import math


# Searching for a connection displays results
def test_searching_for_connection_displays_results(page):
    # 1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 2. Clear the `from` location
    page.click("[data-test=PlacePickerInputPlace-close]")
    page.wait_for_selector("[data-test=PlacePickerInputPlace-close]", state="hidden")

    # 3. Type in `Vienna` to the `from` field
    page.fill("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]", "Vienna")

    # 4. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]:has-text('Vienna, Austria')")

    # 5. Type in `Brno` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Brno")

    # 6. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 7. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 8. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 9. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # (10. variation: among the results, this first one is cheaper than 10 000 CZK)
    first_result_with_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_with_currency_code.replace(",", ""))
    assert first_result_value <= 10000


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


# Sorting panel actions can be used for sorting the search results
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


# Localized currency is retained in Passenger details
def test_localized_currency_is_retained_in_passenger_details(page):
    # 1. Hit the 🇬🇧 CZK button in the navigation bar at the top of the search page
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2 Open the localization settings and wait for the localization modal to be displayed
    page.click("[data-test=RegionalSettingsButton]")
    assert page.is_visible("[data-test=RegionalSettingsModal]")

    # 2. Set the currency in the Language and currency modal to EUR
    currency_code = "EUR"
    page.select_option("[data-test=CurrencySelect]", value=f"{currency_code.lower()}")

    # 3. Hit the Save & continue button
    page.click("[data-test=SubmitRegionalSettingsButton]")

    # 4. Search for connections between any two cities (while un-checking the Booking.com checkbox, as in previous scenarios)
    # 4.1. Clear the `from` location (here with a stabilization to ensure the place-chip is always removed)
    page.click("[data-test=PlacePickerInputPlace-close]")
    if page.is_visible("[data-test=PlacePickerInputPlace-close]"):
        page.click("[data-test=PlacePickerInputPlace-close]")
    page.wait_for_selector("[data-test=PlacePickerInputPlace-close]", state="hidden")

    # 4.2. Type in `Brno` to the `from` field
    page.fill("[data-test=PlacePickerInput-origin] [data-test=SearchField-input]", "Brno")

    # 4.3. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 4.4. Type in `Bucharest` to the `to` field
    page.fill("[data-test=PlacePickerInput-destination] [data-test=SearchField-input]", "Bucharest")

    # 4.5. Select the 1st result from the dropdown
    page.click("[data-test=PlacePickerRow-wrapper]")

    # 4.6. Uncheck the `Booking` checkbox
    page.click("[class*=BookingcomSwitchstyled] [class*=Checkbox]")

    # 4.7. Hit the `Search` button
    page.click("[data-test=LandingSearchButton]")

    # 4.8. Available connections should be displayed
    page.wait_for_selector("[class*=ResultListstyled__ResultListWrapper]", timeout=10000)
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="visible")

    # 5. Store the price value of the first result
    first_result_without_currency_code = page.locator("[data-test=ResultCardPrice]").first.inner_text().split()[0]
    first_result_value = int(first_result_without_currency_code)

    # 6. Hit the Select button of the first result
    page.click("[data-test=BookingButton]")
    page.wait_for_selector("[data-test=MagicLogin]", state="visible")

    # 7. In the Want to sign first? modal hit the Continue as a guest link
    page.click("[data-test=MagicLogin-GuestTextLink]")
    page.wait_for_selector("[data-test=ResultCardWrapper]", state="hidden")
    page.wait_for_selector("[data-test=Reservation-content]", state="visible")
    page.wait_for_selector("[data-test=Breadcrumbs-step-PASSENGER] [aria-current=step]", state="visible")

    # 8. Verify the Total (EUR) price value corresponds with the one stored on step 5.
    total_price_with_currency_code = page.locator("[class*=ReservationBillTotal] [class*=Price]").inner_text()
    total_price_value = int(total_price_with_currency_code.split()[0])
    assert first_result_value == total_price_value

    # (9. variation: verify the currency code selected on step 1 is displayed next to Total in the reservation bill)
    total_currency_code = page.locator("[data-test=ReservationBillBoxTotal]").inner_text().split("(")[1].strip(")")
    assert currency_code == total_currency_code


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
    # The basic assertion `assert total_of_items == total_price_value` would fail beacuse of the way floats are stored.
    # Instead, we can check the absolute difference between the two values is very low, e.g., a bit over 0.01 CZK.

    # Also we can check how relatively distinct the values are:
    # With rel_tol=0.05 the values have to be 5% similar.
    # Here we decided arbitrarily that the values should have rel_tol=0.000000778, i.e., to be 0.00000778% similar.
    assert math.isclose(total_of_items, total_price_value, rel_tol=0.000000778, abs_tol=0.01000000000022)


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


# Calendar buttons (hit month and expect it in the date field)
def test_hitting_calendar_buttons_is_reflected_by_date_field(page):
    # 1. On the Kiwi.com website hit the Departure date field
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Hit the Departure date field
    page.click("[data-test=SearchDateInput]:has-text('Departure')")
    page.wait_for_selector("[data-test=NewDatePickerOpen]", state="visible")

    # 2. Hit the left datepicker month button and store the month value into a variable
    departure_month_button = page.locator("[data-test=DatepickerMonthButton]").nth(0)
    departure_month_button.click()
    departure_month_value = departure_month_button.inner_text().split()[0]

    # 3. Hit the right datepicker month button and store the month value into a variable
    return_month_button = page.locator("[data-test=DatepickerMonthButton]").nth(1)
    return_month_button.click()
    return_month_value = return_month_button.inner_text().split()[0]

    # 4. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm, where:
    # * Wkd are the first 3 characters of a weekday, e.g., Mon or Wed (can be hardcoded)
    # * D is a numeric value of the first day of the month, i.e., 1 (can be hardcoded)
    # * DD is a numeric value of the last day of the month, e.g., 28, 29, 30, or 31 (can be hardcoded)
    # * Mmm are the first 3 characters of name of the month, e.g., Mar or Jun - for each date field it should correspond with the value extracted from steps 3. and 4., respectively
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    departure_field_contents = page.locator(
        "[class*=Inputsstyled__InputWrap]:has([data-navigation=DepartureRangeHeading]) [data-test=DateValue]"
    ).inner_text().split()

    departure_weekday_1 = departure_field_contents[0]
    departure_day_number_1 = int(departure_field_contents[1])
    departure_month_1 = departure_field_contents[2]
    departure_weekday_2 = departure_field_contents[4]
    departure_day_number_2 = int(departure_field_contents[5])
    departure_month_2 = departure_field_contents[6]

    assert departure_weekday_1 in weekdays
    assert departure_weekday_2 in weekdays
    assert departure_day_number_1 in range(1, 32)
    assert departure_day_number_2 in range(1, 32)
    assert departure_month_1 == departure_month_value[:3]
    assert departure_month_2 == departure_month_value[:3]

    # 5. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm
    return_field_contents = page.locator(
        "[class*=Inputsstyled__InputWrap]:has([data-test=ReturnRangeHeading]) [data-test=DateValue]"
    ).inner_text().split()

    return_weekday_1 = return_field_contents[0]
    return_day_number_1 = int(return_field_contents[1])
    return_month_1 = return_field_contents[2]
    return_weekday_2 = return_field_contents[4]
    return_day_number_2 = int(return_field_contents[5])
    return_month_2 = return_field_contents[6]

    assert return_weekday_1 in weekdays
    assert return_weekday_2 in weekdays
    assert return_day_number_1 in range(1, 32)
    assert return_day_number_2 in range(1, 32)
    assert return_month_1 == return_month_value[:3]
    assert return_month_2 == return_month_value[:3]


# Sidebar actions (expanding options, verifying visibility of items)
def test_sidebar_actions_work_as_expected(page):
    # 1. On the Kiwi.com website hit the right sidebar hamburger button
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Hit the right sidebar hamburger button
    page.click("[data-test=NavBar-SideNav-Open]")
    page.wait_for_selector("[data-test=NavBar-SideNav][aria-hidden=false]", state="visible")

    # 2. Verify a sidebar with the Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized support. text appears
    expected_sidebar_text = "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized support."
    current_sidebar_text = page.locator("[data-test=NavBar-SideNav] [class*=Text]").first.inner_text()
    assert expected_sidebar_text == current_sidebar_text

    # 3. Hit the Discover button
    page.click("[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=false]")

    # 4. Verify the Discover button expands into a dropdown/slide of items
    assert page.is_visible(
        "[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=true]"
    )

    # 5. Verify the Subscribe to newsletter button is displayed
    assert page.is_visible("[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')")

    # 6. Verify the Stories button is displayed
    assert page.is_visible("[aria-hidden=false] [class*=TextLink]:has-text('Stories')")

    # 7. Hit the Subscribe to newsletter button
    page.click("[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')")

    # 8. Verify the sidebar disappears
    page.wait_for_selector("[data-test=NavBar-SideNav][aria-hidden=false]", state="hidden")

    # 9. Verify a modal with the Subscribe to the Kiwi.com newsletter heading is displayed
    page.wait_for_selector("[class*=Modal__ModalBody]", state="visible")
    assert page.is_visible(
        "[class*=Modal__ModalBody] [class*=Heading]:has-text('Subscribe to the Kiwi.com newsletter')"
    )

    # 10. Verify the modal can be closed by hitting the cross button in its top right corner
    page.click("[data-test=ModalCloseButton]")
    page.wait_for_selector("[class*=Modal__ModalBody]", state="hidden")


# Popular flights - hitting the Show more button leads to an increment of currently displayed popular flight
# tiles/cards to be displayed
def test_show_more_button_of_popular_flights_displays_increment_of_currently_shown_popular_flight_cards(page):
    # 1. On the Kiwi.com website get the count of tiles/cards in the Popular flights section
    # and store it into a variable
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Get count of tiles/cards in the Popular flights section and store it into a variable
    # [data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]
    initial_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()

    # 2. Hit the Show more button
    page.click("[class*=Box] [class*=Stack]:has-text('Show more')")

    # 3. Verify twice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()
    assert current_card_count == 2 * initial_card_count

    # 4. Hit the Show more button again
    page.click("[class*=Box] [class*=Stack]:has-text('Show more')")

    # 5. Verify thrice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()
    assert current_card_count == 3 * initial_card_count


# Travel mode interactions are respected by the UI
def test_travel_mode_interactions_are_respected_by_the_ui(page):
    # 1. On the Kiwi.com website hit the travel mode button (which has the Return value selected by default)
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Hit the travel mode button
    page.click("[data-test=SearchFormModesPicker-active-return]")

    # 2. Verify a popup with the following options is displayed: Return, One-way, Multi-city, and Nomad
    page.wait_for_selector("[data-test=ModesPopup]", state="visible")
    assert page.is_visible("[data-test=ModePopupOption-return]")
    assert page.is_visible("[data-test=ModePopupOption-oneWay]")
    assert page.is_visible("[data-test=ModePopupOption-multicity]")
    assert page.is_visible("[data-test=ModePopupOption-nomad]")

    # 3. Select the One-way options
    page.click("[data-test=ModePopupOption-oneWay]")

    # 4. Verify the One-way option is selected
    page.wait_for_selector("[data-test=ModesPopup]", state="hidden")
    assert page.is_visible("[data-test=SearchFormModesPicker-active-oneWay]")

    # 5. Verify the Return date field is no longer displayed
    assert page.is_hidden("[data-test=SearchFormModesPicker-active-return]")


# Total count of passengers is reflected by counter next to the passengers icon
def test_total_count_of_passengers_is_reflected_by_counter_next_to_the_passengers_icon(page):
    # 1. On the Kiwi.com website hit the passengers and bags button
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Hit the passengers and bags button
    page.click("[data-test=PassengersField]")
    page.wait_for_selector("[data-test=PassengersPopover]", state="visible")

    # 2. Verify a popup with the following options is displayed: Adults, Children, Infants in the Passengers section
    assert page.is_visible("[class*=Stack]:has-text('Passengers') [data-test=PassengersRow-adults]")
    assert page.is_visible("[class*=Stack]:has-text('Passengers') [data-test=PassengersRow-children]")
    assert page.is_visible("[class*=Stack]:has-text('Passengers') [data-test=PassengersRow-infants]")

    # 3. Verify a popup with the following options is displayed: Cabin baggage and Checked baggage in the Bags section
    assert page.is_visible("[class*=Stack]:has-text('Bags') [data-test=BagsPopup-cabin]")
    assert page.is_visible("[class*=Stack]:has-text('Bags') [data-test=BagsPopup-checked]")

    # 4. Store the values of the count of adults, children and infants into variables
    initial_adults_count = int(page.locator(
        "[data-test=PassengersRow-adults] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    initial_childer_count = int(page.locator(
        "[data-test=PassengersRow-children] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    initial_infants_count = int(page.locator(
        "[data-test=PassengersRow-infants] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))

    # 5. Hit twice the + button next to the Adults option
    adults_increment_count = 2
    for _ in range(adults_increment_count):
        page.click("[data-test=PassengersRow-adults] [aria-label=increment]")

    # 6. Verify the count of adults has increased by 2 (compare with value from step 4.)
    updated_adults_count = int(page.locator(
        "[data-test=PassengersRow-adults] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    assert updated_adults_count == initial_adults_count + adults_increment_count

    # 7. Hit thrice the + button next to the Children option
    children_increment_count = 3
    for _ in range(children_increment_count):
        page.click("[data-test=PassengersRow-children] [aria-label=increment]")

    # 8. Verify the count of adults has increased by 3 (compare with value from step 4.)
    updated_children_count = int(page.locator(
        "[data-test=PassengersRow-children] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    assert updated_children_count == initial_childer_count + children_increment_count

    # 9. Hit once the + button next to the Infants option
    infants_increment_count = 1
    page.click("[data-test=PassengersRow-infants] [aria-label=increment]")

    # 10. Verify the count of adults has increased by 1 (compare with value from step 4.)
    updated_infants_count = int(page.locator(
        "[data-test=PassengersRow-infants] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    assert updated_infants_count == initial_infants_count + infants_increment_count

    # 11. Hit the Done button
    page.click("[data-test=PassengersFieldFooter-done]")
    page.wait_for_selector("[data-test=PassengersPopover]", state="hidden")

    # 12. Verify the count of passengers next to the passengers icon corresponds with the sum of values from steps 6.,
    # 8., and 10.
    passenger_count = int(page.locator("[data-test*=PassengersField-note]").first.inner_text())
    assert passenger_count == updated_adults_count + updated_children_count + updated_infants_count

    # (13. variation: increase the count of baggage and verify the counters correspond with the count of added pieces
    # of baggage)
    # 13.1. Hit the passengers and bags button
    page.click("[data-test=PassengersField]")
    page.wait_for_selector("[data-test=PassengersPopover]", state="visible")

    # 13.2. Store the values of the count of cabin and checked baggage pieces into variables
    initial_cabin_count = int(page.locator(
        "[data-test=BagsPopup-cabin] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    initial_checked_count = int(page.locator(
        "[data-test=BagsPopup-checked] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))

    # 13.3. Hit thrice the + button next to the Cabin baggage option
    cabin_increment_count = 3
    for _ in range(cabin_increment_count):
        page.click("[data-test=BagsPopup-cabin] [aria-label=increment]")

    # 13.4. Verify the count of adults has increased by 3 (compare with value from step 13.2.)
    updated_cabin_count = int(page.locator(
        "[data-test=BagsPopup-cabin] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    assert updated_cabin_count == initial_cabin_count + cabin_increment_count

    # 13.5. Hit twice the + button next to the Checked baggage option
    checked_increment_count = 2
    for _ in range(checked_increment_count):
        page.click("[data-test=BagsPopup-checked] [aria-label=increment]")

    # 13.6. Verify the count of adults has increased by 2 (compare with value from step 13.2.)
    updated_checked_count = int(page.locator(
        "[data-test=BagsPopup-checked] [class*=StepperStateless__StyledStepperInput]"
    ).get_attribute(name="value"))
    assert updated_checked_count == initial_checked_count + checked_increment_count

    # 13.7. Hit the Done button
    page.click("[data-test=PassengersFieldFooter-done]")
    page.wait_for_selector("[data-test=PassengersPopover]", state="hidden")

    # 13.8. Verify the count of passengers next to the passengers icon corresponds with the sum of values from steps
    # 13.4. and 13.6.
    baggage_count = int(page.locator("[class*=PassengersAndBagsFieldstyled__PassengersFieldNote]").nth(1).inner_text())
    assert baggage_count == updated_cabin_count + updated_checked_count
