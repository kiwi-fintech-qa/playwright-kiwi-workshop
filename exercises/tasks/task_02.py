# Interacting with the regional settings and dropdown lists

def test_regional_settings_can_be_changed(page):
	# 1. On the Kiwi.com website and open the regional settings modal
	# Fill in the correct locator-methods where they are missing!

	# 1.1. Open the kiwi.com website and accept cookies
	# Verify that the "Book cheap flights other sites simply can’t find." text is visible.
	page.goto("")
	page.locator("")
	assert page.locator("").is_visible()

	# 1.2. Click open the regional settings modal for currency and language
	page.locator("")

	# 2. Interact with the modal
	# 2.1. From the "Language" dropdown, choose "Dansk" (= Danish)
	page.locator("").select_option("")

	# 2.2. From the "Currency" dropdown, choose Danish Crown
	page.locator("").select_option("")

	# 3. Click the "Save & Continue" button
	page.locator("")
