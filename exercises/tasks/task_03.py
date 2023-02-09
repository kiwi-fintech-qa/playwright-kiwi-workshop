from exercises.tasks.resources.resource_03_04 import open_kiwi_website_and_accept_cookies


# Sidebar actions (expanding options, verifying visibility of items)
def test_sidebar_actions_work_as_expected(page):
    # 1. On the Kiwi.com website hit the right sidebar hamburger button
    # 1.1. Open the kiwi.com website
    open_kiwi_website_and_accept_cookies(page)

    # 1.2. Hit the right sidebar hamburger button
    page.locator("[data-test=]").click()
    page.locator("[data-test=][aria-hidden=]").wait_for(state="")

    # 2. Verify a sidebar with the "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized
    # support." text appears
    current_sidebar_text = page.locator("[data-test=] [class*=]").first.inner_text()
    assert "???" == "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized support."

    # 3. Hit the Discover button
    page.locator("").click()

    # 4. Verify the Discover button expands into a dropdown/slide of items
    assert page.locator("").is_visible()

    # 5. Verify the Subscribe to newsletter button is displayed
    assert page.locator("").is_visible()

    # 6. Verify the Stories button is displayed
    assert page.locator("").is_visible()

    # 7. Hit the Subscribe to newsletter button
    page.locator("").click()

    # 8. Verify the sidebar disappears
    page.locator("[data-test=][aria-hidden=]").wait_for(state="")

    # 9. Verify a modal with the "Subscribe to the Kiwi.com newsletter" heading is displayed
    page.locator("[class*=]").wait_for(state="")
    assert page.locator("").is_visible()

    # 10. Verify the modal can be closed by hitting the cross button in its top right corner
    page.locator("").click()
    page.locator("[class*=]").wait_for(state="")
