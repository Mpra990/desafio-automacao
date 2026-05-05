# 🚀 Desafio de Automação: E2E & API Testing

Este projeto é uma suíte completa de automação de testes voltada para garantir a qualidade de fluxos críticos em aplicações Web e APIs. Ele utiliza um pipeline de **CI/CD** integrado ao GitHub Actions para validação contínua de código.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.14+
*   **Framework de Testes:** Pytest
*   **Automação Web:** Selenium WebDriver
*   **Gerenciamento de Drivers:** WebDriver Manager (Chrome)
*   **Testes de API:** Requests
*   **CI/CD:** GitHub Actions

## 📋 Funcionalidades dos Testes

### 🌐 Automação Web (SauceDemo)
O teste de interface valida o **Caminho Crítico** de um usuário em um e-commerce:
1.  **Autenticação:** Login com credenciais válidas.
2.  **Fluxo de Carrinho:** Adiciona um produto específico (Mochila) ao carrinho.
3.  **Validação de Estado:** Verifica se o contador do carrinho foi atualizado corretamente.
4.  **Limpeza:** Remove o item e confirma se o carrinho voltou ao estado vazio.

### 🔌 Automação de API (PetStore)
Valida a estabilidade e a integridade dos dados do backend:
*   Consulta de inventário da loja.
*   Busca de Pets por status (disponibilidade).
*   Validação de códigos de status HTTP (200 OK).

## ⚙️ Configuração do Ambiente

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/Mpra990/desafio-automacao.git](https://github.com/Mpra990/desafio-automacao.git)