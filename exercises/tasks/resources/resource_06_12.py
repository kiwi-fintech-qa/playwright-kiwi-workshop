class KiwiPage:
    def __init__(self, page):
        self.page = page

        self.cookies_popup_button_accept = page.locator("")
        self.kiwi_page_subtitle = page.locator("")
        self.place_input_chip = page.locator("")
        self.input_field_origin = page.locator("")
        self.input_field_destination = page.locator("")
        self.booking_checkbox = page.locator("").first
        self.regional_settings_button = page.locator("")
        self.regional_settings_modal = page.locator("")
        self.currency_picker = page.locator("")
        self.submit_regional_settings_button = page.locator("")
        self.search_button = page.locator("")
        self.result_list_wrapper = page.locator("")
        self.passengers_and_bags_button = page.locator("")
        self.passengers_and_bags_popup = page.locator("")
        self.passengers_and_bags_done_button = page.locator("")
        self.passenger_row_adults = page.locator("")
        self.passenger_row_children = page.locator("")
        self.passenger_row_infants = page.locator("")
        self.baggage_row_cabin = page.locator("")
        self.baggage_row_checked = page.locator("")
        self.stepper_value_adults = page.locator("")
        self.stepper_value_children = page.locator("")
        self.stepper_value_infants = page.locator("")
        self.stepper_value_cabin_bags = page.locator("")
        self.stepper_value_checked_bags = page.locator("")
        self.stepper_increment_adults = page.locator("")
        self.stepper_increment_children = page.locator("")
        self.stepper_increment_infants = page.locator("")
        self.stepper_increment_cabin_bags = page.locator("")
        self.stepper_increment_checked_bags = page.locator("")
        self.total_passengers = page.locator("").first
        self.total_bags = page.locator("").nth(1)
        self.search_component_departure_field = page.locator("")
        self.date_picker_modal = page.locator("")
        self.departure_month_button = page.locator("").nth(0)
        self.return_month_button = page.locator("").nth(1)
        self.date_picker_modal_departure_field = page.locator("")
        self.date_picker_modal_return_field = page.locator("")

    def open_kiwi_website(self):
        self.page.goto("https://www.kiwi.com/en/")
        self.cookies_popup_button_accept.click()
        assert self.kiwi_page_subtitle.is_visible()

    def clear_the_from_field(self):
        self.place_input_chip.click()
        self.place_input_chip.wait_for(state="")

    def type_origin_location_into_input_field(self, location: str = None):
        self.input_field_origin.fill(location)

    def type_destination_location_into_input_field(self, location: str = None):
        self.input_field_destination.fill(location)

    def select_location_from_dropdown(self, location: str = None):
        self.page.locator(f"[data-test=]:has-text('{location}')").click()

    def uncheck_booking_checkbox(self):
        self.booking_checkbox.click()

    def open_regional_settings(self):
        self.regional_settings_button.click()
        assert self.regional_settings_modal.is_visible()

    def set_currency(self, currency_code: str = None):
        self.currency_picker.select_option(value=f"{currency_code.lower()}")

    def save_regional_settings(self):
        self.submit_regional_settings_button.click()

    def hit_search_button(self):
        self.search_button.click()
        self.result_list_wrapper.wait_for()

    def hit_passengers_and_bags_button(self):
        self.passengers_and_bags_button.click()
        self.passengers_and_bags_popup.wait_for()

    def passenger_types_are_displayed_in_popup(self):
        self.passenger_row_adults.is_visible()
        self.passenger_row_children.is_visible()
        self.passenger_row_infants.is_visible()

    def baggage_types_are_displayed_in_popup(self):
        self.baggage_row_cabin.is_visible()
        self.baggage_row_checked.is_visible()

    def hit_done_button_in_passengers_and_bags_popup(self):
        self.passengers_and_bags_done_button.click()
        self.passengers_and_bags_popup.wait_for(state="hidden")

    def get_count_of_adults(self) -> int:
        adults_count = int(self.stepper_value_adults.get_attribute(name="value"))
        return adults_count

    def get_count_of_children(self) -> int:
        children_count = int(self.stepper_value_children.get_attribute(name="value"))
        return children_count

    def get_count_of_infants(self) -> int:
        infants_count = int(self.stepper_value_infants.get_attribute(name="value"))
        return infants_count

    def get_count_of_cabin_bags(self) -> int:
        cabin_bags_count = int(self.stepper_value_cabin_bags.get_attribute(name="value"))
        return cabin_bags_count

    def get_count_of_checked_bags(self) -> int:
        checked_bags_count = int(self.stepper_value_checked_bags.get_attribute(name="value"))
        return checked_bags_count

    def hit_stepper_increment_button_for_adults(self):
        self.stepper_increment_adults.click()

    def hit_stepper_increment_button_for_children(self):
        self.stepper_increment_children.click()

    def hit_stepper_increment_button_for_infants(self):
        self.stepper_increment_infants.click()

    def hit_stepper_increment_button_for_cabin_bags(self):
        self.stepper_increment_cabin_bags.click()

    def hit_stepper_increment_button_for_checked_bags(self):
        self.stepper_increment_checked_bags.click()

    def get_total_passengers_count(self) -> int:
        total_passengers_count = int(self.total_passengers.inner_text())
        return total_passengers_count

    def get_total_bags_count(self) -> int:
        total_bags_count = int(self.total_bags.inner_text())
        return total_bags_count

    def hit_departure_field_in_the_search_component(self):
        self.search_component_departure_field.click()
        self.date_picker_modal.wait_for()

    def hit_departure_month_button(self):
        self.departure_month_button.click()

    def get_departure_month_value(self) -> str:
        departure_month_value = self.departure_month_button.inner_text().split()[0]
        return departure_month_value

    def hit_return_month_button(self):
        self.return_month_button.click()

    def get_return_month_value(self) -> str:
        return_month_value = self.return_month_button.inner_text().split()[0]
        return return_month_value

    def get_departure_field_contents_from_date_picker_modal(self) -> list[str]:
        departure_field_contents = self.date_picker_modal_departure_field.inner_text().split()
        return departure_field_contents

    def get_return_field_contents_from_date_picker_modal(self) -> list[str]:
        return_field_contents = self.date_picker_modal_return_field.inner_text().split()
        return return_field_contents


class SearchResultPage:
    def __init__(self, page):
        self.page = page

        self.result_card_wrapper = page.locator("").first
        self.first_result_card = page.locator("").first
        self.sort_by_price_button = page.locator("")
        self.sort_by_duration_button = page.locator("")
        self.first_select_card_button = page.locator("").first
        self.sign_in_overlay = page.locator("")
        self.continue_as_guest_link = page.locator("")
        self.reservation_content = page.locator("")
        self.breadcrumbs_current_step_passenger = page.locator()

    def check_a_transport_option_checkbox(self, option: str = None):
        self.page.locator(f"[class*=FilterWrapper]:has([data-test=TransportOptionCheckbox-{option.lower()}])").click()

    def sort_results_by_price(self):
        self.sort_by_price_button.click()

    def sort_results_by_duration(self):
        self.sort_by_duration_button.click()

    def hit_select_button_of_first_result(self):
        self.first_select_card_button.click()
        self.sign_in_overlay.wait_for()

    def hit_continue_as_guest_link(self):
        self.continue_as_guest_link.click()
        self.result_card_wrapper.wait_for(state="hidden")
        self.reservation_content.wait_for()
        self.breadcrumbs_current_step_passenger.wait_for()


class PassengerDetailsPage:
    def __init__(self, page):
        self.page = page

        self.reservation_bill_total = page.locator("")
        self.total_currency_label = page.locator("")
        self.passenger_field_email = page.locator("")
        self.passenger_field_phone = page.locator("")
        self.passenger_field_firstname = page.locator("")
        self.passenger_field_lastname = page.locator("")
        self.passenger_field_birthday = page.locator("")
        self.passenger_field_birthyear = page.locator("")
        self.passenger_field_nationality = page.locator("")
        self.passenger_field_title = page.locator("")
        self.passenger_field_birthmonth = page.locator("")
        self.cabin_baggage_bundle_option = page.locator("")
        self.cabin_baggage_bundle_price = page.locator("")
        self.cabin_baggage_single_item_option = page.locator("")
        self.baggage_empty_option = page.locator("")
        self.checked_baggage_once_option = page.locator("")
        self.checked_baggage_once_price = page.locator("")
        self.checked_baggage_no_bags_checkbox = page.locator("")
        self.no_insurance_option = page.locator("")
        self.continue_button = page.locator("")
        self.previous_step_label_passenger_details = page.locator("")
        self.previous_step_breadcrumb_passenger_details = page.locator("")
        self.current_step_breadcrumb_ticket_fare = page.locator("")
        self.error_highlight = page.locator("").first
        self.current_step_breadcrumb_passenger_details = page.locator("")
        self.error_field_email = page.locator("")
        self.error_field_phone = page.locator("").first
        self.error_field_firstname = page.locator("")
        self.error_field_lastname = page.locator("")
        self.error_field_nationality = page.locator("")
        self.error_field_gender = page.locator("")
        self.error_field_birthdate = page.locator("")

    def fill_out_passenger_email(self, email: str = None):
        self.passenger_field_email.fill(email)

    def fill_out_passenger_phone(self, phone: str = None):
        self.passenger_field_phone.fill(phone)

    def fill_out_passenger_firstname(self, firstname: str = None):
        self.passenger_field_firstname.fill(firstname)

    def fill_out_passenger_lastname(self, lastname: str = None):
        self.passenger_field_lastname.fill(lastname)

    def fill_out_passenger_birthday(self, birthday: str = None):
        self.passenger_field_birthday.fill(birthday)

    def fill_out_passenger_birthyear(self, birthyear: str = None):
        self.passenger_field_birthyear.fill(birthyear)

    def select_passenger_nationality(self, nationality: str = None):
        self.passenger_field_nationality.select_option(value=nationality)

    def select_passenger_title(self, title: str = None):
        self.passenger_field_title.select_option(value=title)

    def select_passenger_birthmonth(self, birthmonth: str = None):
        self.passenger_field_birthmonth.select_option(value=birthmonth)

    def select_cabin_baggage_bundle(self):
        self.cabin_baggage_bundle_option.click()

    def select_cabin_baggage_single_item(self):
        self.cabin_baggage_single_item_option.click()

    def get_carry_on_baggage_price_value_from_baggage_section(self) -> float:
        carry_on_baggage_price_with_currency_code = self.cabin_baggage_bundle_price.inner_text()
        carry_on_baggage_price_value = None
        return carry_on_baggage_price_value

    def select_checked_baggage_once(self):
        self.checked_baggage_once_option.click()

    def select_no_checked_baggage_checkbox(self):
        self.checked_baggage_no_bags_checkbox.click()

    def get_checked_baggage_price_value_from_baggage_section(self) -> float:
        checked_baggage_price_with_currency_code = self.checked_baggage_once_price.inner_text()
        checked_baggage_price_value = None
        return checked_baggage_price_value

    def select_no_insurance(self):
        self.no_insurance_option.click()

    def proceed_to_ticket_fare_page(self):
        self.continue_button.click()
        self.previous_step_label_passenger_details.wait_for()
        self.previous_step_breadcrumb_passenger_details.wait_for()
        self.current_step_breadcrumb_ticket_fare.wait_for()

    def hit_continue_button_and_expect_to_stay_on_passenger_details_due_to_error(self):
        self.continue_button.click()
        self.error_highlight.wait_for()
        self.current_step_breadcrumb_passenger_details.wait_for()

    def wait_for_email_error_to_be_displayed(self):
        self.error_field_email.wait_for()

    def wait_for_email_error_to_not_be_displayed(self):
        self.error_field_email.wait_for(state="hidden")

    def phone_field_error_should_be_displayed(self):
        assert self.error_field_phone.is_visible()

    def phone_field_error_should_not_be_displayed(self):
        assert self.error_field_phone.is_hidden()

    def first_name_error_should_be_displayed(self):
        assert self.error_field_firstname.is_visible()

    def first_name_error_should_not_be_displayed(self):
        assert self.error_field_firstname.is_hidden()

    def last_name_error_should_be_displayed(self):
        assert self.error_field_lastname.is_visible()

    def last_name_error_should_not_be_displayed(self):
        assert self.error_field_lastname.is_hidden()

    def nationality_error_should_be_displayed(self):
        assert self.error_field_nationality.is_visible()

    def nationality_error_should_not_be_displayed(self):
        assert self.error_field_nationality.is_hidden()

    def gender_error_should_be_displayed(self):
        assert self.error_field_gender.is_visible()

    def gender_error_should_not_be_displayed(self):
        assert self.error_field_gender.is_hidden()

    def birthdate_error_should_be_displayed(self):
        assert self.error_field_birthdate.is_visible()

    def birthdate_error_should_not_be_displayed(self):
        assert self.error_field_birthdate.is_hidden()


class TicketFarePage:
    def __init__(self, page):
        self.page = page

        self.reservation_bill_carry_on_baggage_price = page.locator("")
        self.reservation_bill_checked_baggage_price = page.locator("")
        self.reservation_bill_passenger_price = page.locator("")
        self.reservation_bill_total_price = page.locator("")

    # Replace the None-assignment in the below methods with an assignment which will return the expected value instead
    # Hint: Use the built-in Python functions float(), split() and replace()

    def get_carry_on_baggage_price_value_from_reservation_bill(self) -> float:
        total_carry_on_baggage_price_with_currency_code = self.reservation_bill_carry_on_baggage_price.inner_text()
        total_carry_on_baggage_price_value = None
        return total_carry_on_baggage_price_value

    def get_checked_baggage_price_value_from_reservation_bill(self) -> float:
        total_checked_baggage_price_with_currency_code = self.reservation_bill_checked_baggage_price.inner_text()
        total_checked_baggage_price_value = None
        return total_checked_baggage_price_value

    def get_passenger_price_value_from_reservation_bill(self) -> float:
        total_passenger_price_with_currency_code = self.reservation_bill_passenger_price.inner_text()
        total_passenger_price_value = None
        return total_passenger_price_value

    def get_total_price_value_from_reservation_bill(self) -> float:
        total_price_with_currency_code = self.reservation_bill_total_price.inner_text()
        total_price_value = None
        return total_price_value
