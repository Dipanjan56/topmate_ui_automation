from behave import *
from features.pageobjects.PublicProfile_BookingFormPage import PublicProfileBookingFormPage
from features.pageobjects.PublicProfile_Webinar_Package_BookingPage import PublicProfileWebinarPackageBookingPage
from utilities import log_util

log = log_util.get_logs()


@when("user clicks on Book Seat")
def step_impl(context):
    booking_type = 'Webinar'
    context.public_profile_webinar_seat_booking_page = PublicProfileWebinarPackageBookingPage(context.driver,
                                                                                              booking_type)
    context.public_profile_webinar_seat_booking_page.book_seat_for_webinar()


@step("user fills up the booking form for webinar service with user details")
def step_impl(context):
    booking_type = 'webinar'
    booking_duration = None
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_webinar(row['Your Name'],
                                                                                             row['Email'],
                                                                                             row['Phone Number'])


@step("user clicks on Confirm Details")
def step_impl(context):
    context.public_profile_booking_form_page.user_click_on_confirm_details()