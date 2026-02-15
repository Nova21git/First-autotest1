from playwright.sync_api import Page
from pages.select_page import SelectPage
import allure


@allure.feature('Select')
@allure.story('Выбор Python из выпадающего списка')
def test_select_python(page: Page):
    """
    Тест: Выбрать Python из выпадающего списка и проверить результат
    """
    select_page = SelectPage(page)

    select_page.open()
    select_page.should_have_choose_language_text()
    select_page.select_python()
    select_page.submit()
    select_page.should_see_selected_python()