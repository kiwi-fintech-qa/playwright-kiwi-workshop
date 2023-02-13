from exercises.tasks.resources.resource_06_12 import KiwiPage, SearchResultPage


# Searching with additional transportation options shows results cheaper than 2 000 CZK
def test_searching_with_additional_transportation_options_shows_results_cheaper_than_1k_czk(page):
    # 1. Steps 1-9. from the previous scenario
    # 1.1. Open the kiwi.com website (wait for page to load) and accept cookies
    kiwi_page = KiwiPage(page)

    # 1.2. Clear the "from" location

    # 1.3. Type in "Vienna" to the "from" field

    # 1.4. Select the "Vienna, Austria" result from the dropdown

    # 1.5. Type in "Brno" to the "to" field

    # 1.6. Select the "Brno, Czechia" result from the dropdown

    # 1.7. Uncheck the "Booking" checkbox

    # 1.8. Hit the "Search" button

    # 1.9. Available connections should be displayed
    search_result_page = SearchResultPage(page)

    # 2. Check the "Bus" checkbox in the "Transport" left-hand section of the results

    # 3. Verify the first result is cheaper than 2 000 CZK

    # (4. variation: on step 2. check the "Train" checkbox in the "Transport" left-hand section as well; on step 3. verify the results are cheaper than 400 CZK)
    # 4.1 Check the "Train" checkbox in the "Transport" left-hand section as well

    # 4.2 Verify the results are cheaper than 500 CZK
