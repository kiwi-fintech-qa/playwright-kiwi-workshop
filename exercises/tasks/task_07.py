from exercises.tasks.resources.resource_06_12 import KiwiPage, SearchResultPage


# Localized currency is retained in Passenger details
def test_localized_currency_is_retained_in_passenger_details(page):
    # 1. Hit the 🇬🇧 CZK button in the navigation bar at the top of the search page
    # 1.1. Open the kiwi.com website and accept cookies
    pass

    # 1.2 Open the localization settings and wait for the localization modal to be displayed

    # 2. Set the currency in the Language and currency modal to "EUR"

    # 3. Hit the Save & continue button

    # 4. Search for connections between any two cities
    # 4.1. Clear the "from" location (here with a stabilization to ensure the place-chip is always removed)

    # 4.2. Type in "Brno" to the "from" field

    # 4.3. Select the "Brno, Czechia" result from the dropdown

    # 4.4. Type in "Vienna" to the "to" field

    # 4.5. Select the "Vienna, Austria" result from the dropdown

    # 4.6. Uncheck the "Booking" checkbox

    # 4.7. Hit the "Search" button

    # 4.8. Available connections should be displayed

    # 5. Store the price value of the first result

    # 6. Hit the "Select" button of the first result

    # 7. In the "Want to sign first?" modal hit the "Continue as a guest link"

    # 8. Verify the "Total" ("EUR") price value corresponds with the one stored on step 5.

    # (9. variation: verify the currency code selected on step 1 is displayed next to "Total" in the reservation bill)
