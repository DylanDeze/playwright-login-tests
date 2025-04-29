from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime

BASE_URL = "https://practicetestautomation.com/practice-test-login/"
GOOD_USERNAME = "student"
GOOD_PASSWORD = "Password123"
NEGATIVE_USERNAME = "incorrectUser"
NEGATIVE_PASSWORD = "incorrectPassword"
PARENT_DIRECTORY = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIRECTORY = Path(PARENT_DIRECTORY / "screenshots")
SCREENSHOTS_DIRECTORY.mkdir(parents=True, exist_ok=True)

def fill_and_submit_login(page, username, password):
    page.wait_for_selector('//input[@id="username"]').type(username)
    page.wait_for_selector('//input[@id="password"]').type(password)
    page.wait_for_selector('//button[@id="submit"]').click()

def save_screenshot(page, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = SCREENSHOTS_DIRECTORY / f"{name}_{timestamp}.png"
    page.screenshot(path=screenshot_path, full_page=True)

def test_login_success(page):
    page.goto(BASE_URL)
    fill_and_submit_login(page, GOOD_USERNAME, GOOD_PASSWORD)
    try:
        assert page.locator("text=Logged In Successfully").is_visible(), "Login success message not visible"
    except Exception as e:
        save_screenshot(page, "test_login_success_error")
        raise e

def test_login_invalid_username(page):
    page.goto(BASE_URL)
    fill_and_submit_login(page, NEGATIVE_USERNAME, GOOD_PASSWORD)
    try:
        assert page.locator('//div[@id="error"]').is_visible(), "Error message for invalid username not visible"
    except Exception as e:
        save_screenshot(page, "test_login_invalid_username_error")
        raise e

def test_login_invalid_password(page):
    page.goto(BASE_URL)
    fill_and_submit_login(page, GOOD_USERNAME, NEGATIVE_PASSWORD)
    try:
        assert page.locator('//div[@id="error"]').is_visible(), "Error message for invalid password not visible"
    except Exception as e:
        save_screenshot(page, "test_login_invalid_password_error")
        raise e

# Main runner
if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        tests = [
            ("test_login_success", test_login_success),
            ("test_login_invalid_username", test_login_invalid_username),
            ("test_login_invalid_password", test_login_invalid_password),
        ]

        for name, test_func in tests:
            try:
                test_func(page)
                print(f"✅ {name} passed", flush=True)
            except Exception as e:
                print(f"❌ {name} failed: {e}", flush=True)
        browser.close()
