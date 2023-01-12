import math


# Filling out paid baggage options on Passenger details is reflected by the reservation bill
def test_filling_out_paid_baggage_options_on_passenger_details_is_reflected_by_the_reservation_bill(page):
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

    # 4. Fill out the Email, Phone, Given names, Surnames and the DD and YYYY fields of Date of birth as follows:
    # 4.1. Email: play@wrig.ht

    # 4.2. Phone: 123123123

    # 4.3. Given names: Play

    # 4.4. Surnames: Wright

    # 4.5. DD: 1

    # 4.6. YYYY: 1901

    # 5. In the following dropdowns select the following values:
    # 5.1. Nationality: United Kingdom

    # 5.2. Gender: Female

    # 5.3. Month: January

    # 6. In the Cabin or carry-on baggage section select the Carry-on bundle option and store its price value

    # 7. In the Checked baggage section select the 1× checked bag option and store its price value

    # 8. In the Travel insurance section select the No insurance option

    # 9. Hit the Continue button and verify the Ticker fare screen is displayed

    # 10. Verify the following items are displayed in the reservation bill:
    # 10.1. Cabin baggage: value stored at step 6
    total_carry_on_baggage_price_value = 0

    # 10.2. Checked baggage: value stored at step 7
    total_checked_baggage_price_value = 0

    # (11. variation: verify the total price corresponds with the sum of all items in the reservation bill)
    total_passenger_price_value = 0
    total_price_value = 0

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
