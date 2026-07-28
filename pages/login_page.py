import time
from pages.base_page import BasePage
from playwright.sync_api import expect




class LoginPage(BasePage):

    OH = "text = OHIF Viewer"
    Invalid_username_error = "div[class='cds--actionable-notification__content']"
    Invalid_username_error_keycloak = "div[id='input-error-username']"
    Invalid_password_error_keycloak = "div[id='input-error-password']"
    Title_Text = "//h6[text()='Dashboard']"





    ########## From here, define methods to interact with the elements defined above ##########

    def open_login(self):
        self.login()

    def validate_title_text(self):
        expect(self.page.locator(self.Title_Text)).to_have_text("Dashboard")