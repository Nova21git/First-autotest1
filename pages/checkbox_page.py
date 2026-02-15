from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

# Локаторы для страницы с чекбоксами
CHECKBOX_LOCATOR = 'input[type="checkbox"]'  # Сам чекбокс
CHECKBOX_LABEL_FOR = 'label[for="id_checkbox_0"]'  # ИСПРАВЛЕНО
SUBMIT_BUTTON = 'input[type="submit"]'  # Кнопка Submit
RESULT_LOCATOR = '#result-text'  # Текст результата


class CheckboxPage(BasePage):
    """Page Object для страницы https://www.qa-practice.com/elements/checkbox/single_checkbox"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://www.qa-practice.com/elements/checkbox/single_checkbox'

    @allure.step("Открыть страницу с чекбоксом")
    def open(self):
        super().open()
        return self

    @allure.step("Проверить, что чекбокс имеет правильный текст")
    def should_have_correct_label(self):
        """Проверяет, что текст рядом с чекбоксом — 'Select me or not'."""
        label = self.page.locator(CHECKBOX_LABEL_FOR)
        label_text = label.text_content().strip()
        assert "Select me or not" in label_text, f"Текст '{label_text}' не содержит 'Select me or not'"
        return self

    @allure.step("Отметить чекбокс")
    def check_checkbox(self):
        checkbox = self.page.locator(CHECKBOX_LOCATOR)
        checkbox.check()
        return self

    @allure.step("Снять отметку с чекбокса")
    def uncheck_checkbox(self):
        checkbox = self.page.locator(CHECKBOX_LOCATOR)
        checkbox.uncheck()
        return self

    @allure.step("Проверить, что чекбокс отмечен")
    def should_be_checked(self):
        checkbox = self.page.locator(CHECKBOX_LOCATOR)
        expect(checkbox).to_be_checked()
        return self

    @allure.step("Проверить, что чекбокс НЕ отмечен")
    def should_be_unchecked(self):
        checkbox = self.page.locator(CHECKBOX_LOCATOR)
        expect(checkbox).not_to_be_checked()
        return self

    @allure.step("Нажать кнопку Submit")
    def click_submit(self):
        submit = self.page.locator(SUBMIT_BUTTON)
        submit.click()
        return self

    @allure.step("Проверить, что результат отображается и содержит текст чекбокса")
    def should_see_result_with_text(self, expected_text: str = "select me or not"):
        """
        Проверяет, что после отправки формы с отмеченным чекбоксом,
        результат виден и содержит ожидаемый текст.
        """
        result = self.page.locator(RESULT_LOCATOR)
        expect(result).to_be_visible()
        # На сайте текст с маленькой буквы: "select me or not"
        actual_text = result.text_content().strip()
        assert actual_text == expected_text, f"Ожидали '{expected_text}', получили '{actual_text}'"
        return self

    @allure.step("Проверить, что результат НЕ отображается")
    def should_not_see_result(self):
        """
        Проверяет, что после отправки формы без отметки чекбокса,
        результат не появляется.
        """
        assert self.page.locator(RESULT_LOCATOR).count() == 0, "Результат не должен отображаться"
        return self