from playwright.sync_api import sync_playwright, expect

"""
В данном задании вам необходимо написать скрипт, который выполнит следующие действия:

Откроет страницу регистрации.
Проверит, что кнопка "Registration" находится в состоянии disabled.
Заполнит форму регистрации.
Убедится, что кнопка "Registration" стала доступной для взаимодействия (enabled).
Шаги выполнения скрипта:

Открыть страницу регистрации: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration.
Проверить, что кнопка "Registration" находится в состоянии disabled.
Заполнить поле Email значением: user.name@gmail.com.
Заполнить поле Username значением: username.
Заполнить поле Password значением: password.
Проверить, что кнопка "Registration" перешла в состояние enabled.
Требования к скрипту:  registration-page-registration-button
"""
# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка registration не активна
    login_button = page.get_by_test_id('registration-page-registration-button')
    expect(login_button).to_be_disabled()

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmailcom")

    # Находим поле "username" и заполняем его
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')  # locator оставлен специально
    password_input.fill("password")

    # Проверяем, кнопка "Registration" перешла в состояние enabled
    login_button = page.get_by_test_id('registration-page-registration-button')
    expect(login_button).to_be_enabled()

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
