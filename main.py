import pyautogui
import time
import pandas




# Passo 1: Abrir o sistema da empresa
# Pressiona Alt e depois Tab pra trocar de janela
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https:/login") # Local fictício, coloque o certo
pyautogui.press("enter")
time.sleep(1)
pyautogui.PAUSE = 0.5



# Passo 2: Fazer login

pyautogui.click(x=808, y=298)
pyautogui.write("seu_email_aqui")
pyautogui.press('tab')
pyautogui.write('abcd1234')
pyautogui.press('tab')
pyautogui.press('enter')


# Passo 3: Importar a base de dados dos produtos

tabela = pandas.read_csv("caminho_do_csv")
display(tabela)


# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    # pyautogui.click(x=847, y=220) -> Use o pyautogui.displayposition() para achar o local correto de onde deve clicar
    # e tire os hashtags daqui
    
    # Código
    codigo = tabela.loc[linha, 'código']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # Marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # Categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # Custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Observação
    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)
# Passo 5: Repetir o passo 4 até acabar todos os produtos
