from playwright.sync_api import Page,expect

def test_simple_exists(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_visible()

def test_simple_click(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')
    button = page.locator('#submit-id-submit')
    button.click()
    result = page.locator('#result-text')
    expect(result).to_have_text('Submitted')