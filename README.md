# Preenchimento Automático de Google Forms com Python 📝🤖

Este projeto é um script de automação que preenche formulários do Google Forms automaticamente, lendo perguntas e opções a partir de um arquivo `.txt`.

## Funcionalidades 🚀

- Lê perguntas e opções de um arquivo de texto estruturado
- Preenche campos no Google Forms utilizando PyAutoGUI
- Insere perguntas com opções formatadas
- Automatiza múltiplas perguntas com facilidade

## Tecnologias usadas 🛠️

- Python 3.x
- PyAutoGUI
- Pyperclip
- Expressões Regulares (Regex)

## Como usar 📂

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/preenchimento-automatico-google-forms.git
cd preenchimento-automatico-google-forms
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Edite o arquivo `perguntas.txt` com suas perguntas no seguinte formato:

```
Questão 1: Qual é a capital do Brasil?
Brasília
Rio de Janeiro
São Paulo
Belo Horizonte

Questão 2: Qual é 2 + 2?
3
4
5
```

4. Execute o script:

```bash
python preencher_forms.py
```

5. Você terá **5 segundos para abrir o Google Forms** e posicionar o cursor no primeiro campo antes da automação começar.

## ⚠️ Observações:

- O script simula teclado e mouse, então **não mexa no computador enquanto ele estiver rodando**.
- O layout do Google Forms pode sofrer pequenas variações, ajustes podem ser necessários.

## Licença 📄

Este projeto está sob a licença MIT.

---

