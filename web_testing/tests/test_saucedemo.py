import time
import pytest
from selenium.webdriver.common.by import By
from web_testing.pages.login_page import LoginPage

# --- TESTE 1: CAMINHO NEGATIVO (SENHA INCORRETA) ---
def test_login_senha_invalida(driver):
    """Valida se o sistema bloqueia acesso com senha errada"""
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    
    login.realizar_login("standard_user", "senha_qualquer")
    
    # Validação da mensagem de erro
    msg_erro = login.obter_mensagem_erro()
    assert "Username and password do not match" in msg_erro
    time.sleep(2)

# --- TESTE 2: FUNCIONALIDADE DE REMOÇÃO (CARRINHO) ---
def test_remover_produto_do_carrinho(driver):
    """Valida se o usuário consegue desistir de um item no carrinho"""
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")

    # Adiciona e depois remove
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # Valida se o badge do carrinho sumiu (está vazio)
    carrinho_vazio = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(carrinho_vazio) == 0
    time.sleep(2)

# --- TESTE 3: VALIDAÇÃO DE FILTROS (ORDENAÇÃO) ---
def test_ordenar_produtos_por_preco(driver):
    """Valida se o filtro de 'Preço: Menor para Maior' funciona"""
    login = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login.realizar_login("standard_user", "secret_sauce")

    # Seleciona o filtro
    seletor = driver.find_element(By.CLASS_NAME, "product_sort_container")
    seletor.send_keys("Price (low to high)")
    
    # Pega o preço do primeiro produto da lista
    primeiro_preco = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    # O item mais barato da SauceDemo é $7.99
    assert "$7.99" in primeiro_preco
    time.sleep(2)