from exercises.solutions.resources.resource_03_04 import open_kiwi_website_and_accept_cookies


# Travel mode interactions are respected by the UI
def test_travel_mode_interactions_are_respected_by_the_ui(page):
    # 1. On the Kiwi.com website hit the travel mode button (which has the Return value selected by default)
    # 1.1. Open the kiwi.com website
    open_kiwi_website_and_accept_cookies(page)

    # 1.2. Hit the travel mode button
    page.locator("[data-test=SearchFormModesPicker-active-return]").click()

    # 2. Verify a popup with the following options is displayed: Return, One-way, Multi-city, and Nomad
    page.locator("[data-test=ModesPopup]").wait_for(state="visible")
    assert page.locator("[data-test=ModePopupOption-return]").is_visible()  # the Return option is visible
    assert page.locator("[data-test=ModePopupOption-oneWay]").is_visible()  # the One-way option is visible
    assert page.locator("[data-test=ModePopupOption-multicity]").is_visible()  # the Multi-city option is visible
    assert page.locator("[data-test=ModePopupOption-nomad]").is_visible()  # the Nomad option is visible

    # 3. Select the One-way options
    page.locator("[data-test=ModePopupOption-oneWay]").click()

    # 4. Verify the One-way option is selected
    page.locator("[data-test=ModesPopup]").wait_for(state="hidden")
    assert page.locator("[data-test=SearchFormModesPicker-active-oneWay]").is_visible()

    # 5. Verify the Return date field is no longer displayed
    assert page.locator("[data-test=SearchFormModesPicker-active-return]").is_hidden()
