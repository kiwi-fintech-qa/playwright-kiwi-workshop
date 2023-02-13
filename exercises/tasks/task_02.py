# Popular flights - hitting the Show more button leads to an increment of currently displayed popular flight
# tiles/cards to be displayed
def test_show_more_button_of_popular_flights_displays_increment_of_currently_shown_popular_flight_cards(page):
    # 1. On the Kiwi.com website get the count of tiles/cards in the Popular flights section
    # and store it into a variable
    # 1.1. Open the kiwi.com website (https://www.kiwi.com/en/) and accept cookies and
    # verify that the "Book cheap flights other sites simply can’t find." text is displayed.
    page.goto("")
    page.locator("").click()
    assert page.locator("text=").is_visible()

    # 1.2. Get count of tiles/cards in the Popular flights section and store it into a variable
    initial_card_count = page.locator("[data-test=] [class*=]").count()

    # 2. Hit the Show more button
    page.locator("").click()

    # 3. Verify twice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=] [class*=]").count()
    assert "???" == 2 * "???"

    # 4. Hit the Show more button again
    page.locator("").click()

    # 5. Verify thrice the count of tiles/cards from step 1. is displayed
    current_card_count = page.locator("[data-test=] [class*=]").count()
    assert "???" == 3 * "???"
