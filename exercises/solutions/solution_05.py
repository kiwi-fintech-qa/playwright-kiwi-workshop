from exercises.solutions.resources.resource_04_05 import (
    open_kiwi_website_and_accept_cookies,
)


# Interacting with the sidebar (expanding options, verifying visibility of items)
def test_sidebar_actions_work_as_expected(page):
    # 1. On the Kiwi.com website hit the right sidebar hamburger button
    # Fill in the correct locator-methods where they are missing!

    # 1.1. Open the kiwi.com website and accept cookies
    open_kiwi_website_and_accept_cookies(page)

    # 1.2. Click the right sidebar hamburger button and wait for the sidebar to be visible
    page.locator("[data-test=NavBar-SideNav-Open]").click()
    page.locator("[data-test=NavBar-SideNav][aria-hidden=false]").wait_for(
        state="visible"
    )

    # 2. Verify that a sidebar with the "Manage your trips, set up price alerts, use Kiwi.com Credit, and get
    # personalized support." text appears
    expected_sidebar_text = "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized support."
    current_sidebar_text = page.locator(
        "[data-test=NavBar-SideNav] [class*=Text]"
    ).first.inner_text()
    assert expected_sidebar_text == current_sidebar_text

    # 2.1 (Optional) Consider how you could make the above assertion fit the line length restriction of 120 characters?
    page.pause()

    # 3. Click the "Discover" button
    page.locator(
        "[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=false]"
    ).click()

    # 4. Verify the dropdown list of items becomes visible / expanded
    assert page.locator(
        "[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=true]"
    ).is_visible()

    # 5. Verify the "Subscribe to newsletter" button is visible
    assert page.locator(
        "[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')"
    ).is_visible()

    # 6. Verify the "Stories" button is visible
    assert page.locator(
        "[aria-hidden=false] [class*=TextLink]:has-text('Stories')"
    ).is_visible()

    # 7. Click the "Subscribe to newsletter" button
    page.locator(
        "[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')"
    ).click()

    # 8. Verify the sidebar disappears
    page.locator("[data-test=NavBar-SideNav] [aria-hidden=false]").wait_for(
        state="hidden"
    )

    # 9. Verify a modal with the "Subscribe to the Kiwi.com newsletter" heading is visible
    page.locator("[class*=Modal__ModalBody]").wait_for(state="visible")
    assert page.locator(
        "[class*=Modal__ModalBody] [class*=Heading]:has-text('Subscribe to the Kiwi.com newsletter')"
    ).is_visible()

    # 10. Verify the modal can be closed by clicking the cross button in its top right corner
    page.locator("[data-test=ModalCloseButton]").click()
    page.locator("[class*=Modal__ModalBody]").wait_for(state="hidden")
