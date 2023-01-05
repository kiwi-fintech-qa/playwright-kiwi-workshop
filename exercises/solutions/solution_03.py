from exercises.solutions.resources.resource_03_04 import open_kiwi_website


# Sidebar actions (expanding options, verifying visibility of items)
def test_sidebar_actions_work_as_expected(page):
    # 1. On the Kiwi.com website hit the right sidebar hamburger button
    # 1.1. Open the kiwi.com website
    open_kiwi_website(page)

    # 1.2. Hit the right sidebar hamburger button
    # TODO: rewrite into page.locator form instead of just the obsolete page form
    page.click("[data-test=NavBar-SideNav-Open]")
    page.wait_for_selector("[data-test=NavBar-SideNav][aria-hidden=false]", state="visible")

    # 2. Verify a sidebar with the "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized
    # support." text appears
    expected_sidebar_text = "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized support."
    current_sidebar_text = page.locator("[data-test=NavBar-SideNav] [class*=Text]").first.inner_text()
    assert expected_sidebar_text == current_sidebar_text

    # 3. Hit the Discover button
    page.click("[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=false]")

    # 4. Verify the Discover button expands into a dropdown/slide of items
    assert page.is_visible(
        "[data-test=NavBar-SideNav][aria-hidden=false] [role=button]:has-text('Discover') [aria-expanded=true]"
    )

    # 5. Verify the Subscribe to newsletter button is displayed
    assert page.is_visible("[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')")

    # 6. Verify the Stories button is displayed
    assert page.is_visible("[aria-hidden=false] [class*=TextLink]:has-text('Stories')")

    # 7. Hit the Subscribe to newsletter button
    page.click("[aria-hidden=false] [class*=TextLink]:has-text('Subscribe to newsletter')")

    # 8. Verify the sidebar disappears
    page.wait_for_selector("[data-test=NavBar-SideNav][aria-hidden=false]", state="hidden")

    # 9. Verify a modal with the "Subscribe to the Kiwi.com newsletter" heading is displayed
    page.wait_for_selector("[class*=Modal__ModalBody]", state="visible")
    assert page.is_visible(
        "[class*=Modal__ModalBody] [class*=Heading]:has-text('Subscribe to the Kiwi.com newsletter')"
    )

    # 10. Verify the modal can be closed by hitting the cross button in its top right corner
    page.click("[data-test=ModalCloseButton]")
    page.wait_for_selector("[class*=Modal__ModalBody]", state="hidden")
