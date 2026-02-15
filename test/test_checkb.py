from playwright.sync_api import Page
from pages.checkbox_page import CheckboxPage
import allure

@allure.feature('Checkbox')
@allure.story('Проверка выделения и отправки')
def test_checkbox_select_and_submit(page: Page):
    """
    1. Открыть страницу
    2. Отметить чекбокс
    3. Нажать Submit
    4. Проверить, что результат отображается с текстом чекбокса
    """
    checkbox_page = CheckboxPage(page)

    checkbox_page.open()
    checkbox_page.should_have_correct_label()
    checkbox_page.check_checkbox()
    checkbox_page.should_be_checked()
    checkbox_page.click_submit()
    checkbox_page.should_see_result_with_text("select me or not")


@allure.feature('Checkbox')
@allure.story('Проверка снятия отметки')
def test_checkbox_can_be_unchecked(page: Page):
    """
    Проверить, что чекбокс можно отметить и снять отметку.
    """
    checkbox_page = CheckboxPage(page)

    checkbox_page.open()
    checkbox_page.should_be_unchecked()  # По умолчанию не отмечен
    checkbox_page.check_checkbox()
    checkbox_page.should_be_checked()    # Отметили
    checkbox_page.uncheck_checkbox()
    checkbox_page.should_be_unchecked()  # Сняли отметку


@allure.feature('Checkbox')
@allure.story('Проверка отправки без выбора')
def test_submit_without_selection(page: Page):
    """
    1. Открыть страницу
    2. НЕ отмечать чекбокс
    3. Нажать Submit
    4. Проверить, что результат НЕ отображается
    """
    checkbox_page = CheckboxPage(page)

    checkbox_page.open()
    checkbox_page.should_be_unchecked()  # Убедимся, что не отмечен
    checkbox_page.click_submit()
    checkbox_page.should_not_see_result()  # Результата быть не должно