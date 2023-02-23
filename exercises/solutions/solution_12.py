from exercises.solutions.resources.resource_07_12 import KiwiPage


# Total count of passengers is reflected by counter next to the passengers icon
def test_total_count_of_passengers_is_reflected_by_counter_next_to_the_passengers_icon(page):
    # 1. On the Kiwi.com website hit the passengers and bags button
    # 1.1. Open the kiwi.com website and accept cookies
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website_and_accept_cookies()

    # 1.2. Hit the passengers and bags button
    kiwi_page.hit_passengers_and_bags_button()

    # 2. Verify a popup with the following options is displayed: Adults, Children, Infants in the Passengers section
    kiwi_page.passenger_types_are_displayed_in_popup()

    # 3. Verify a popup with the following options is displayed: Cabin baggage and Checked baggage in the Bags section
    kiwi_page.baggage_types_are_displayed_in_popup()

    # 4. Store the values of the count of adults, children and infants into variables
    initial_adults_count = kiwi_page.get_count_of_adults()
    initial_children_count = kiwi_page.get_count_of_children()
    initial_infants_count = kiwi_page.get_count_of_infants()

    # 5. Hit twice the + button next to the Adults option
    adults_increment_count = 2
    for _ in range(adults_increment_count):
        kiwi_page.hit_stepper_increment_button_for_adults()

    # 6. Verify the count of adults has increased by 2 (compare with value from step 4.)
    updated_adults_count = kiwi_page.get_count_of_adults()
    assert updated_adults_count == initial_adults_count + adults_increment_count

    # 7. Hit thrice the + button next to the Children option
    children_increment_count = 3
    for _ in range(children_increment_count):
        kiwi_page.hit_stepper_increment_button_for_children()

    # 8. Verify the count of adults has increased by 3 (compare with value from step 4.)
    updated_children_count = kiwi_page.get_count_of_children()
    assert updated_children_count == initial_children_count + children_increment_count

    # 9. Hit once the + button next to the Infants option
    infants_increment_count = 1
    kiwi_page.hit_stepper_increment_button_for_infants()

    # 10. Verify the count of adults has increased by 1 (compare with value from step 4.)
    updated_infants_count = kiwi_page.get_count_of_infants()
    assert updated_infants_count == initial_infants_count + infants_increment_count

    # 11. Hit the Done button
    kiwi_page.hit_done_button_in_passengers_and_bags_popup()

    # 12. Verify the count of passengers next to the passengers icon corresponds with the sum of values from steps 6.,
    # 8., and 10.
    passenger_count = kiwi_page.get_total_passengers_count()
    assert passenger_count == updated_adults_count + updated_children_count + updated_infants_count

    # (13. variation: increase the count of baggage and verify the counters correspond with the count of added pieces
    # of baggage)
    # 13.1. Hit the passengers and bags button
    kiwi_page.hit_passengers_and_bags_button()

    # 13.2. Store the values of the count of cabin and checked baggage pieces into variables
    initial_cabin_count = kiwi_page.get_count_of_cabin_bags()
    initial_checked_count = kiwi_page.get_count_of_checked_bags()

    # 13.3. Hit thrice the + button next to the Cabin baggage option
    cabin_increment_count = 3
    for _ in range(cabin_increment_count):
        kiwi_page.hit_stepper_increment_button_for_cabin_bags()

    # 13.4. Verify the count of adults has increased by 3 (compare with value from step 13.2.)
    updated_cabin_count = kiwi_page.get_count_of_cabin_bags()
    assert updated_cabin_count == initial_cabin_count + cabin_increment_count

    # 13.5. Hit twice the + button next to the Checked baggage option
    checked_increment_count = 2
    for _ in range(checked_increment_count):
        kiwi_page.hit_stepper_increment_button_for_checked_bags()

    # 13.6. Verify the count of adults has increased by 2 (compare with value from step 13.2.)
    updated_checked_count = kiwi_page.get_count_of_checked_bags()
    assert updated_checked_count == initial_checked_count + checked_increment_count

    # 13.7. Hit the Done button
    kiwi_page.hit_done_button_in_passengers_and_bags_popup()

    # 13.8. Verify the count of bags next to the baggage icon corresponds with the sum of values from steps
    # 13.4. and 13.6.
    baggage_count = kiwi_page.get_total_bags_count()
    assert baggage_count == updated_cabin_count + updated_checked_count
