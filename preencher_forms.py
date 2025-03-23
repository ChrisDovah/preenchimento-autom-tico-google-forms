import pyautogui
import pyperclip
import time
import re

pyautogui.PAUSE = 0.5

def escrever(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

def ler_arquivo(arquivo):
    perguntas = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = [linha.strip() for linha in file.readlines() if linha.strip()]

    pergunta_atual = None
    opcoes = []

    for linha in linhas:
        if re.match(r"^Questão \d+: ", linha):
            if pergunta_atual:
                perguntas.append({"pergunta": pergunta_atual, "opcoes": opcoes})
                opcoes = []
            pergunta_atual = linha.split(": ", 1)[1]
        else:
            opcoes.append(linha)

    if pergunta_atual:
        perguntas.append({"pergunta": pergunta_atual, "opcoes": opcoes})

    return perguntas

def preencher_google_forms(perguntas):
    for i, item in enumerate(perguntas):
        escrever(item["pergunta"])
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'b')
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        time.sleep(0.5)
        
        for i, opcao in enumerate(item["opcoes"]):
            escrever(opcao)
            if i < len(item["opcoes"]) - 1:
                pyautogui.press("enter")
                time.sleep(0.5)
        
        for _ in range(10):
            pyautogui.press("tab")
        time.sleep(1)

arquivo_perguntas = "perguntas.txt"
perguntas = ler_arquivo(arquivo_perguntas)

print("Você tem 5 segundos para abrir o Google Forms e colocar o cursor no primeiro campo.")
time.sleep(5)

preencher_google_forms(perguntas)
print("Formulário preenchido automaticamente!")
