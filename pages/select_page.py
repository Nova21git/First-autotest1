from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

# Локаторы
SELECT_FIELD = '#id_choose_language'
SUBMIT_BUTTON = '#submit-id-submit'
RESULT_TEXT = '#result'


class SelectPage(BasePage):
    """Page Object для страницы с выпадающим списком"""

    url = 'https://www.qa-practice.com/elements/select/single_select'

    def _select(self):
        return self.page.locator(SELECT_FIELD)

    def _result(self):
        return self.page.locator(RESULT_TEXT)

    @allure.step("Открыть страницу с выпадающим списком")
    def open(self):
        super().open()
        self.page.wait_for_selector(SELECT_FIELD, state="visible", timeout=10000)
        return self

    @allure.step("Проверить наличие надписи 'Choose language'")
    def should_have_choose_language_text(self):
        expect(self.page.locator('body')).to_contain_text("Choose language")
        return self

    @allure.step("Выбрать язык Python")
    def select_python(self):
        expect(self._select()).to_be_visible()
        self._select().select_option(label="Python")
        return self

    @allure.step("Нажать кнопку Submit")
    def submit(self):
        self.page.locator(SUBMIT_BUTTON).click()
        return self

    @allure.step("Проверить результат 'You selected Python'")
    def should_see_selected_python(self):
        """Проверяет, что появилась надпись 'You selected Python'"""
        expect(self._result()).to_be_visible(timeout=10000)
        # to_have_text автоматически игнорирует лишние пробелы и переносы
        expect(self._result()).to_have_text("You selected Python")
        return self