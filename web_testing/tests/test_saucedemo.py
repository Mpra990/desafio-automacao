import pytest
import time
from selenium.webdriver.common.by import By

def test_fluxo_compra_completo(driver):
    # 1. Acessar o site e fazer Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # 2. Adicionar a Mochila (Backpack) ao Carrinho
    # O ID do botão é específico para este produto
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # 3. Validar se o ícone do carrinho mostra '1' item (Badge)
    carrinho_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrinho_badge.text == "1"
    
    # 4. Abrir o carrinho
    carrinho_badge.click()
    time.sleep(1) # Pequena pausa para visualização e carregamento da página
    
    # 5. Remover o item do carrinho
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # 6. Sincronização: Aguardar o sistema processar a remoção
    time.sleep(1) 
    
    # 7. Validar que o carrinho está vazio 
    # (O elemento 'shopping_cart_badge' deve desaparecer do HTML)
    itens_no_carrinho = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(itens_no_carrinho) == 0