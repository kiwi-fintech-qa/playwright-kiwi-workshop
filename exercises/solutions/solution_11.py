# Total count of passengers is reflected by counter next to the passengers icon
def test_total_count_of_passengers_is_reflected_by_counter_next_to_the_passengers_icon(page):
    # 1. On the Kiwi.com website hit the passengers and bags button
    # 1.1. Open the kiwi.com website (wait for page to load)
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
