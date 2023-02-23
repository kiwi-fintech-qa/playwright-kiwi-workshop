from exercises.tasks.resources.resource_04_05 import (
    open_kiwi_website_and_accept_cookies,
)


# Travel mode interactions are respected by the UI
def test_travel_mode_interactions_are_respected_by_the_ui(page):
    # 1. On the Kiwi.com website hit the travel mode button (which has the "Return" value selected by default)
    # Fill in the correct locator-methods where they are missing!

    # 1.1. Open the kiwi.com website and accept cookies

    # 1.2. Click the travel mode button
    page.locator("")

    # 2. Verify a popup with the following options is displayed: Return, One-way, Multi-city, and Nomad
    page.locator("").wait_for(state="")
    assert page.locator("")  # the Return option is visible
    assert page.locator("")  # the One-way option is visible
    assert page.locator("")  # the Multi-city option is visible
    assert page.locator("")  # the Nomad option is visible

    # 3. Select the "One-way" option
    page.locator("")

    # 4. Verify the "One-way" option is selected and visible
    page.locator("").wait_for(state="")
    assert page.locator("")

    # 5. Verify the "Return date" field is no longer visible
    assert page.locator("").is_hidden()
