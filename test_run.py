def test_try_my_luck(page):
	page.goto("https://www.google.com/")
	page.locator("text=Reject all").nth(1).click()
	page.locator("[aria-label*='Feeling Lucky']").nth(1).click()
