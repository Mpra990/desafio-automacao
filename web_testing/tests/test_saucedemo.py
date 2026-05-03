from web_testing.pages.login_page import LoginPage

def test_login_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_login_invalido(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("user_errado", "senha_errada")
    # Verifica se a mensagem de erro aparece
    assert len(driver.find_elements("css selector", ".error-message-container")) > 0