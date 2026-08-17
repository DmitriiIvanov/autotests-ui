from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmailcom")

    # Находим поле "username" и заполняем его
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input') #locator оставлен специально
    password_input.fill("password")

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
    title_dashboard_alert = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title_dashboard_alert).to_be_visible()  # Проверяем видимость элемента
    expect(title_dashboard_alert).to_have_text("Dashboard")  # Проверяем текст

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
