from selenium.webdriver.common.by import By

class LoginPage:
    """Encapsula os elementos da tela de login (Padrão Page Objects)"""
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        # CORREÇÃO AQUI: Usamos CSS_SELECTOR para pegar o atributo data-test
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']") 

    def realizar_login(self, usuario, senha):
        """Método reutilizável para login"""
        self.driver.find_element(*self.username_field).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(senha)
        self.driver.find_element(*self.login_button).click()

    def obter_mensagem_erro(self):
        """Retorna o texto do erro quando o login falha"""
        return self.driver.find_element(*self.error_message).text