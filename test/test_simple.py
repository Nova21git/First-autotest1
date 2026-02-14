from playwright.sync_api import Page
from pages.simple_page import SimplePage
import allure
@allure.feature('Simple button')
def test_simple_exists(page: Page):
    simpl_page = SimplePage(page)
    simpl_page.open()
    simpl_page.check_button_exists()

def test_simple_click(page: Page):
    simpl_page = SimplePage(page)
    simpl_page.open()
    simpl_page.click_button()
    simpl_page.check_result_text_is_('Submitted')