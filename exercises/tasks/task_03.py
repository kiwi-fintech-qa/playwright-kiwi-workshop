# Popular flights - hitting the Show more button leads to an increment of currently displayed popular flight
# tiles/cards to be displayed
def test_show_more_button_of_popular_flights_displays_increment_of_currently_shown_popular_flight_cards(page):
    # 1. On the Kiwi.com website get the total count of visible tiles/cards in the "Popular flights" section
    # and store it into a variable
    # Fill in the correct locator-methods where they are missing!

    # 1.1. Open the kiwi.com website and accept cookies
    page.goto("")
    page.locator("").click()

    # 1.2. Get the count of tiles/cards in the "Popular flights" section and store it into a variable
    initial_card_count = page.locator("[data-test=] [class*=]").count()

    # 2. Click the "Show more" button
    page.locator("")

    # 3. Verify the count of tiles/cards from step 1. is doubled
    current_card_count = page.locator("[data-test=] [class*=]").count()
    assert "???" == 2 * "???"

    # 4. Click the "Show more" button again
    page.locator("")

    # 5. Verify the count of tiles/cards from step 1. is tripled
    current_card_count = page.locator("[data-test=] [class*=]").count()
    assert "???" == 3 * "???"
