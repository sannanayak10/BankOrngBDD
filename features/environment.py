from playwright.sync_api import sync_playwright
from app_config.config import BROWSER, HEADLESS
import os
import datetime
import allure

p = None
browser = None


def before_all(context):
    global p, browser
    p = sync_playwright().start()

    if BROWSER == 'chromium':
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=100, args=["--start-maximized"])
    elif BROWSER == 'firefox':
        browser = p.firefox.launch(headless=HEADLESS, slow_mo=500, args=["--start-maximized"])
    else:
        browser = p.webkit.launch(headless=HEADLESS)

    context._playwright = p
    context._browser = browser


def before_scenario(context, scenario):

    context.context = context._browser.new_context(ignore_https_errors=True,
        viewport=None
    )

    context.page = context.context.new_page()




def after_scenario(context, scenario):
    # Take screenshot if test fails and attach to Allure report
    if scenario.status == "failed":
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        filename = f"{scenario.name.replace(' ', '_')}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)

        # Take screenshot
        context.page.screenshot(path=filepath, full_page=True)
        print(f"Test failed. Screenshot saved: {filepath}")

        #Attach screenshot to Allure report
        with open(filepath, "rb") as image_file:
            allure.attach(image_file.read(), name=scenario.name, attachment_type=allure.attachment_type.PNG)

    context.page.close()
    context.context.close()




def after_all(context):
    context._browser.close()
    context._playwright.stop()
