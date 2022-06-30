import datetime
import pyautogui
import time
import schedule

atual = datetime.datetime.now() #busca a data atual e armazena em "atual"

dateToday = atual.strftime('%d.%m.%Y') # converte a data em string e formata para o formato D/M/Y formato padrao é Y/M/D estando armazenada na variavel (dateToday)
def trocaData(): #funcao que altera a data
    #coloca data
    pyautogui.moveTo(834, 68, 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(dateToday)
    pyautogui.press('TAB')
    time.sleep(0.5)
    pyautogui.moveTo(1327, 60, 0.5)
    pyautogui.click()
    time.sleep(0.5)
    print('eu executei - trocaData') # teste pra ver se funcao é executada
    
def buscar(): #funcao de autoclick que busca e atualiza de 10 em 10 min
    #busca
    pyautogui.moveTo(1327, 60, 0.5)
    pyautogui.click()
    print('eu executei - buscar') # teste pra ver se funcao é executada

# modulo de cronograma para executar as tarefas.
schedule.every(10).minute.do(buscar)
schedule.every().day.at('08:00').do(trocaData)
schedule.every().day.at('15:00').do(trocaData)

while True: # Laço infinito que verifica se algum cronograma precisa ser executado
    schedule.run_pending()
    time.sleep(60)
    



