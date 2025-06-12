# TDD-TESTE_SW
# Calculadora de Imposto de Renda com TDD

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/coverage-100%25-green?style=flat&logo=pytest)

## Sobre o Projeto

Este projeto é uma atividade acadêmica para a disciplina de **Teste de Software**. O objetivo foi desenvolver uma calculadora de Imposto de Renda de Pessoa Física (IRPF), aplicando na prática a metodologia de **Desenvolvimento Orientado a Testes (TDD)**.

Todo o desenvolvimento foi guiado por testes, seguindo o ciclo **Red-Green-Refactor** para garantir a corretude e a manutenibilidade do código.

---

## Funcionalidades

A calculadora implementa as seguintes funcionalidades:

- ✔️ Cadastrar múltiplos rendimentos (salários, aluguéis, etc.).
- ✔️ Cadastrar múltiplas deduções (previdência, dependentes, pensão, etc.).
- ✔️ Calcular o valor total dos rendimentos.
- ✔️ Calcular o valor total das deduções.
- ✔️ Determinar a base de cálculo do imposto (Rendimentos - Deduções).
- ✔️ Calcular o valor do imposto devido, com base nas faixas de alíquota da tabela do IRPF.
- ✔️ Calcular a alíquota efetiva do imposto.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework de Testes:** Pytest

---

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

- Python 3.10 ou superior
- Git

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/rmatuda/TDD-TESTE_SW.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd TDD-TESTE_SW
    ```

3.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate

    # Ativa o ambiente (Linux/macOS)
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todos os pacotes necessários. Para instalá-los, execute:
    ```bash
    pip install -r requirements.txt
    ```

### Executando os Testes

Para verificar se toda a lógica está funcionando corretamente, execute os testes com o Pytest:

```bash
pytest
```

A saída esperada é que todos os testes passem com sucesso.
