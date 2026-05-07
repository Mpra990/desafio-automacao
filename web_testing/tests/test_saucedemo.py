import time
import pytest
from selenium.webdriver.common.by import By
from web_testing.pages.login_page import LoginPage

# 1. CAMINHO FELIZ: COMPRA COMPLETA
def test_fluxo_compra_e2e(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("M")
    driver.find_element(By.ID, "last-name").send_keys("Pra")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    assert "Thank you for your order" in driver.find_element(By.CLASS_NAME, "complete-header").text

# 2. CAMINHO NEGATIVO: SENHA ERRADA
def test_login_senha_invalida(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "senha_errada")
    assert "Username and password do not match" in login.obter_mensagem_erro()

# 3. CAMINHO NEGATIVO: ACESSO SEM LOGIN (CORRIGIDO)
def test_seguranca_acesso_direto(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    login = LoginPage(driver)
    # Ajustado de "after" para "when" para bater certinho com o site
    assert "You can only access '/inventory.html' when you are logged in" in login.obter_mensagem_erro()

# 4. FUNCIONALIDADE: REMOVER DO CARRINHO
def test_remover_do_carrinho(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

# 5. LÓGICA: FILTRO DE PREÇO
def test_filtro_preco_baixo_alto(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")
    driver.find_element(By.CLASS_NAME, "product_sort_container").send_keys("Price (low to high)")
    preco = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert "$7.99" in preco

# 6. INTEGRIDADE: VALIDAR NOME NO CARRINHO
def test_validar_nome_item_no_carrinho(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_nome = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_nome == "Sauce Labs Backpack"

# 7. SESSÃO: LOGOUT
def test_realizar_logout(driver):
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1) # Espera a animação do menu
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert driver.find_element(By.ID, "login-button").is_displayed()