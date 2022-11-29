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
