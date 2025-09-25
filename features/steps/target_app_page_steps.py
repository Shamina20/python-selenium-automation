

from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.target_app_page.open_signin_page()


@when('Store original window')
def store_window(context):
    context.original_window=context.app.target_app_page.get_original_window()
    print("Original window is:",context.original_window)


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions(context):
    context.app.target_app_page.click_tc_link()
    sleep(3)


@when('Switch to the newly opened window')
def switch_window(context):
    # current_windows=context.driver.window_handles
    # new_window=current_windows[1]
    # context.driver.switch_to.window(new_window)
    context.app.target_app_page.switch_to_newly_opened_window([context.original_window])

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()


@then('User can close new window and switch back to original')
def user_close_new_window(context):
    context.app.terms_conditions_page.close()
    sleep(3)
    context.app.terms_conditions_page.switch_to_window_by_id(context.original_window)
    sleep(3)