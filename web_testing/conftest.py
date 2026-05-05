import pytest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    
    # DESATIVA TOTALMENTE O SERVIÇO DE VERIFICAÇÃO DE SENHAS VAZADAS
    options.add_argument("--disable-features=SafeBrowsing")
    options.add_argument("--disable-features=PasswordLeakDetection")
    
    # Bloqueia pop-ups e o gerenciador de senhas
    options.add_experimental_option("prefs", {
        "password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
    })
    
    # Evita que o Chrome pergunte sobre ser o navegador padrão
    options.add_argument("--no-default-browser-check")
    
    if platform.system() == "Windows":
        pass 
    else:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()