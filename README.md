# 🧪 Desafio de Automação: API & Web Testing
> Status do Projeto: Finalizado e Homologado ✅

Este repositório contém a solução para o desafio de automação de testes, integrando testes de interface (Web) com Selenium e testes de serviços (API) com Requests, utilizando Python e Pytest.

---

## 🎯 Objetivo
Validar a robustez dos fluxos principais da plataforma **SauceDemo** e da API **PetStore**, garantindo a integridade dos dados, segurança de acesso e a experiência do usuário através de testes de "Caminho Feliz" e "Caminhos de Exceção".

## 🚀 Tecnologias e Ferramentas
* **Python 3.14+**: Linguagem base.
* **Pytest**: Framework de execução de testes.
* **Selenium WebDriver**: Automação de interface.
* **Requests**: Automação de chamadas REST API.
* **Page Object Model (POM)**: Padrão de projeto para manutenibilidade.
* **GitHub Actions**: Pipeline de CI/CD para execução automática.

---

## 📂 Arquitetura do Projeto
A estrutura foi desenhada para separar a lógica de negócio dos scripts de teste:

```text
├── .github/workflows/  # Configuração da automação no GitHub (CI)
├── api_testing/        # Testes de API REST
│   └── tests/          # Cenários Pet, Store e User
├── web_testing/        # Testes de Interface Web
│   ├── pages/          # Elementos e Métodos (Page Objects)
│   └── tests/          # Cenários de Fluxo de Compra e Segurança
├── conftest.py         # Fixtures e configurações do Navegador
└── requirements.txt    # Lista de dependências do projeto📑 Plano de Testes Executados

🌐 Automação Web (7 Cenários)
Compra Completa (E2E): Fluxo total desde o login até o "Thank You".

Login com Senha Inválida: Validação de segurança e mensagem de erro.

Segurança de Acesso: Bloqueia acesso via URL direta sem autenticação.

Remoção de Itens: Teste de manipulação dinâmica do carrinho.

Filtro por Preço: Valida a lógica de ordenação (Menor para Maior).

Integridade do Item: Garante que o nome do item não mude no carrinho.

Fluxo de Logout: Encerramento seguro da sessão.

📡 Automação de API (6 Cenários)
Pet: Criação (POST) e tratamento de erro 404 (GET).

Store: Consulta de inventário e criação de novos pedidos.

User: Cadastro de novo usuário e teste de autenticação (Login).
💻 Guia de Configuração (Para o Usuário)
Para rodar este projeto localmente, siga estes passos:

1. Pré-requisitos
Python 3.10 ou superior: Instalado e adicionado ao PATH do sistema.

Google Chrome: Instalado (o driver será gerenciado automaticamente pelo código).

Git: Para clonar o repositório.

2. Passo a Passo de Instalação
No terminal da pasta do projeto, execute:

Criar o Ambiente Virtual (Isolamento):

PowerShell
python -m venv .venv
Ativar o Ambiente:

No Windows: .\.venv\Scripts\Activate.ps1

No Mac/Linux: source .venv/bin/activate

Instalar as Dependências:

PowerShell
pip install -r requirements.txt
3. Execução dos Testes
Para rodar todos os testes e ver o relatório no terminal:

PowerShell
pytest -v -s
💡 O que você precisa explicar na apresentação:
Se o professor perguntar: "O que eu preciso para rodar isso no meu PC?", você responde com estes 3 pilares técnicos:

Ambiente Virtual (venv):

"Professor, eu utilizei um ambiente virtual para garantir que as bibliotecas do projeto não entrem em conflito com outras versões do Python que você possa ter na sua máquina. Isso isola as dependências."

Gerenciamento de Drivers (WebDriver Manager):

"Não é necessário baixar o chromedriver.exe manualmente. Eu implementei o webdriver-manager no arquivo conftest.py. Ele detecta a versão do seu Chrome e baixa o driver compatível automaticamente no momento da execução."

Arquivo de Requisitos (requirements.txt):

"Todas as bibliotecas necessárias (Selenium, Pytest, Requests) estão mapeadas no arquivo requirements.txt. Basta um único comando pip install para configurar tudo."

✅ Checklist Final no seu VS Code:
Antes de fechar tudo, verifique se o arquivo requirements.txt na raiz do projeto está exatamente assim:

Plaintext
selenium
pytest
requests
webdriver-manager
E garanta que seu conftest.py está usando o ChromeDriverManager, pois é ele que faz a mágica de funcionar em qualquer computador sem precisar configurar caminhos de arquivos manualmente.

Com isso, seu projeto está "Portátil" e pronto para ser avaliado em qualquer máquina! 🚀