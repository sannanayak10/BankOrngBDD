import time

from behave import given, then, when
from pages.login_page import LoginPage


@given('I login with username')
def step_open_worklist_tab(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.open_login()

@then('Validate the tilte text')
def step_validate_tilte_text(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.validate_title_text()


@given('the user is on login page')
def step_login_page(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.login_page()


@when('the user enters an invalid username')
def step_user_enters_invalid_username(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.invalid_username()

@then('the user clicks on the Login button')
def step_user_enters_login_button(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.enter_login_button()

@then('the system should display an error message for invalid username')
def step_system_should_display_error_message(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.invalid_username_error_popup()

@when('the user enters an invalid username in keycloak')
def step_user_enters_invalid_username_in_keycloak(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.invalid_username_in_keycloak()

@then('the system should display an error message for invalid username on keycloak page')
def step_system_should_display_error_message_in_keycloak(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.invalid_username_error_popup_keycloak()


@when('the user enters an valid username and invalid password in keycloak')
def step_user_enters_valid_username_and_invalid_password(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.valid_username_and_invali_password_in_keycloak()


@then('the system should display an error message for valid username and invalid password on keycloak page')
def step_system_should_display_error_message_in_keycloak(context):
    context.login_obj = LoginPage(context.page)
    context.login_obj.invalid_password_error_popup_keycloak()
