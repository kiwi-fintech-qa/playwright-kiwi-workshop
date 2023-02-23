from exercises.tasks.resources.resource_07_12 import KiwiPage, SearchResultPage


# Sorting panel actions can be used for sorting the search results
def test_sorting_panel_actions_can_be_used_for_sorting_the_search_results(page):
    # 1. Steps 1.1.-1.9. from the previous task

    # 1.1. Open the kiwi.com website and accept cookies

    # 1.2. Clear the "from" location

    # 1.3. Type in "Brno" to the "from" field

    # 1.4. Select the "Brno, Czechia" result from the dropdown

    # 1.5. Type in "Vienna" to the "to" field

    # 1.6. Select the "Vienna, Austria" result from the dropdown

    # 1.7. Uncheck the "Booking" checkbox

    # 1.8. Hit the "Search" button

    # 1.9. Available connections should be displayed

    # 2. Check the "Train" checkbox in the "Transport" left-hand section of the results

    # 3. Select the "Cheapest" sorting option from the sorting panel

    # 4. Store the price value of the first few (e.g., 3) results into a (Python) list
    result_values_list = []
    for i in range(3):
        nth_result_with_currency_code = page.locator("").nth(i).inner_text().split()[0]
        nth_result_value = int(nth_result_with_currency_code.replace(",", ""))
        result_values_list.append(nth_result_value)

    # 5. Verify the first result is either the cheapest of the stored values, or the same as the rest of them

    # (6. variation: on step 3. select the "Fastest" sorting option; on step 5. identify the cheapest of the stored
    # results [i.e., identify the cheapest of the several fastest connections)
    # 6.1. Select the "Fastest" sorting option

    # 6.2. Identify the cheapest of the several fastest connections
