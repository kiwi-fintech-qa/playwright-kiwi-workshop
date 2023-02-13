# Popular flights - hitting the Show more button leads to an increment of currently displayed popular flight
# tiles/cards to be displayed
def test_show_more_button_of_popular_flights_displays_increment_of_currently_shown_popular_flight_cards(page):
    # 1. On the Kiwi.com website get the count of tiles/cards in the Popular flights section
    # and store it into a variable
    # 1.1. Open the kiwi.com website (https://www.kiwi.com/en/) and accept cookies
    page.goto("https://www.kiwi.com/en/")
    page.locator("[data-test='CookiesPopup-Accept']").click()
    assert page.locator("text=Book cheap flights other sites simply can’t find.").is_visible()

    # 1.2. Get count of tiles/cards in the Popular flights section and store it into a variable
    initial_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()

    # 2. Hit the Show more button
    page.locator("[class*=Box] [class*=Stack]:has-text('Show more')").click()

    # 3. Verify twice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()
    assert current_card_count == 2 * initial_card_count

    # 4. Hit the Show more button again
    page.locator("[class*=Box] [class*=Stack]:has-text('Show more')").click()

    # 5. Verify thrice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=PopularFlights] [class*=PopularFlightCardstyled__Card]").count()
    assert current_card_count == 3 * initial_card_count
