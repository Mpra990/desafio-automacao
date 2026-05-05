import pytest
import time
from selenium.webdriver.common.by import By

def test_fluxo_compra_completo(driver):
    # 1. Acessar o site oficial do desafio
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) # Pausa para o público ver a tela de carregamento
    
    # 2. Realizar o Login
    # Preenchendo o campo de usuário
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1) # Pausa para mostrar a digitação
    
    # Preenchendo o campo de senha
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1) # Pausa para mostrar a digitação
    
    # Clicando no botão de Login
    driver.find_element(By.ID, "login-button").click()
    
    # PAUSA CRÍTICA: Aguarda 4 segundos para garantir que o Chrome ignore 
    # o alerta de "senha vazada" e carregue a vitrine de produtos.
    time.sleep(4) 
    
    # 3. Adicionar a Mochila (Backpack) ao Carrinho
    # Este passo falhou anteriormente porque a tela de alerta bloqueou o clique.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("Produto adicionado com sucesso!")
    time.sleep(2) # Pausa para ver o botão mudar de 'Add to cart' para 'Remove'
    
    # 4. Abrir a página do Carrinho clicando no ícone superior
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2) # Pausa para o público ver o item listado no carrinho
    
    # 5. Remover o item para limpar o teste
    # Isso demonstra que o script consegue interagir com elementos dinâmicos.
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    print("Produto removido para limpar o ambiente.")
    time.sleep(2) # Pausa para observar a lista ficando vazia
    
    # 6. Validação final: o contador de itens (badge) não deve existir
    itens_no_carrinho = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(itens_no_carrinho) == 0
    
    print("\n✅ Sucesso: O fluxo foi executado e validado visualmente!")
    time.sleep(1)