import time
import os
from playwright.sync_api import Page


from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read values from .env
MAIN_URL = os.getenv("MAIN_URL")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")


class BasePage:

    def __init__(self, page: Page):
        self.page = page



    def login(self):
        self.page.goto(MAIN_URL
,timeout=60000,
        wait_until="domcontentloaded"
)
        #self.page.wait_for_load_state("networkidle")
        self.page.get_by_placeholder("Username").type(USER_NAME)
        #self.page.locator("button[data-testid='login-button']").click()
        #self.page.locator("input[id='username']").type(USER_NAME)
        self.page.get_by_placeholder("Password").type(USER_PASSWORD)
        self.page.locator("//button[@type='submit']").click()
       # self.page.locator("paper-button[id='desktoploginModes']").click()
        #self.page.wait_for_load_state("networkidle")