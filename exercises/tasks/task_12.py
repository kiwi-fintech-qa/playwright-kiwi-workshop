from exercises.tasks.resources.resource_06_12 import KiwiPage, SearchResultPage


# Calendar buttons (hit month and expect it in the date field)
def test_hitting_calendar_buttons_is_reflected_by_date_field(page):
    # 1. On the Kiwi.com website hit the Departure date field
    # 1.1. Open the kiwi.com website and accept cookies
    pass

    # 1.2. Hit the Departure date field

    # 2. Hit the left datepicker month button and store the month value into a variable

    # 3. Hit the right datepicker month button and store the month value into a variable

    # 4. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm, where:
    # * Wkd are the first 3 characters of a weekday, e.g., Mon or Wed (can be hardcoded)
    # * D is a numeric value of the first day of the month, i.e., 1 (can be hardcoded)
    # * DD is a numeric value of the last day of the month, e.g., 28, 29, 30, or 31 (can be hardcoded)
    # * Mmm are the first 3 characters of name of the month, e.g., Mar or Jun - for each date field it should correspond
    #   with the value extracted from steps 3. and 4., respectively

    # 5. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm
