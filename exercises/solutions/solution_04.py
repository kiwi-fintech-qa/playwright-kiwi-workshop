# Travel mode interactions are respected by the UI
def test_travel_mode_interactions_are_respected_by_the_ui(page):
    # 1. On the Kiwi.com website hit the travel mode button (which has the Return value selected by default)
    # 1.1. Open the kiwi.com website (wait for page to load)
    page.goto("https://www.kiwi.com/en/")
    page.click("[data-test='CookiesPopup-Accept']")
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")

    # 1.2. Hit the travel mode button
    page.click("[data-test=SearchFormModesPicker-active-return]")

    # 2. Verify a popup with the following options is displayed: Return, One-way, Multi-city, and Nomad
    page.wait_for_selector("[data-test=ModesPopup]", state="visible")
    assert page.is_visible("[data-test=ModePopupOption-return]")
    assert page.is_visible("[data-test=ModePopupOption-oneWay]")
    assert page.is_visible("[data-test=ModePopupOption-multicity]")
    assert page.is_visible("[data-test=ModePopupOption-nomad]")

    # 3. Select the One-way options
    page.click("[data-test=ModePopupOption-oneWay]")

    # 4. Verify the One-way option is selected
    page.wait_for_selector("[data-test=ModesPopup]", state="hidden")
    assert page.is_visible("[data-test=SearchFormModesPicker-active-oneWay]")

    # 5. Verify the Return date field is no longer displayed
    assert page.is_hidden("[data-test=SearchFormModesPicker-active-return]")
