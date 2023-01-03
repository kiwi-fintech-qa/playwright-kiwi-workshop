from exercises.solutions.resource_06_12 import KiwiPage


# Calendar buttons (hit month and expect it in the date field)
def test_hitting_calendar_buttons_is_reflected_by_date_field(page):
    # 1. On the Kiwi.com website hit the Departure date field
    # 1.1. Open the kiwi.com website (wait for page to load)
    kiwi_page = KiwiPage(page)
    kiwi_page.open_kiwi_website()

    # 1.2. Hit the Departure date field
    kiwi_page.hit_departure_field_in_the_search_component()

    # 2. Hit the left datepicker month button and store the month value into a variable
    kiwi_page.hit_departure_month_button()
    departure_month_value = kiwi_page.get_departure_month_value()

    # 3. Hit the right datepicker month button and store the month value into a variable
    kiwi_page.hit_return_month_button()
    return_month_value = kiwi_page.get_return_month_value()

    # 4. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm, where:
    # * Wkd are the first 3 characters of a weekday, e.g., Mon or Wed (can be hardcoded)
    # * D is a numeric value of the first day of the month, i.e., 1 (can be hardcoded)
    # * DD is a numeric value of the last day of the month, e.g., 28, 29, 30, or 31 (can be hardcoded)
    # * Mmm are the first 3 characters of name of the month, e.g., Mar or Jun - for each date field it should correspond with the value extracted from steps 3. and 4., respectively
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    departure_field_contents = kiwi_page.get_departure_field_contents_from_date_picker_modal()

    departure_weekday_1 = departure_field_contents[0]
    departure_day_number_1 = int(departure_field_contents[1])
    departure_month_1 = departure_field_contents[2]
    departure_weekday_2 = departure_field_contents[4]
    departure_day_number_2 = int(departure_field_contents[5])
    departure_month_2 = departure_field_contents[6]

    assert departure_weekday_1 in weekdays
    assert departure_weekday_2 in weekdays
    assert departure_day_number_1 in range(1, 32)
    assert departure_day_number_2 in range(1, 32)
    assert departure_month_1 == departure_month_value[:3]
    assert departure_month_2 == departure_month_value[:3]

    # 5. Verify the Departure field contains a string in the following format: Wkd D Mmm – Wkd DD Mmm
    return_field_contents = kiwi_page.get_return_field_contents_from_date_picker_modal()

    return_weekday_1 = return_field_contents[0]
    return_day_number_1 = int(return_field_contents[1])
    return_month_1 = return_field_contents[2]
    return_weekday_2 = return_field_contents[4]
    return_day_number_2 = int(return_field_contents[5])
    return_month_2 = return_field_contents[6]

    assert return_weekday_1 in weekdays
    assert return_weekday_2 in weekdays
    assert return_day_number_1 in range(1, 32)
    assert return_day_number_2 in range(1, 32)
    assert return_month_1 == return_month_value[:3]
    assert return_month_2 == return_month_value[:3]
