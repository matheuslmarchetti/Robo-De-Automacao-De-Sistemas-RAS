import pyautogui
import os
import time

# Mensagem de alerta para iniciar RAS
pyautogui.alert("""
    Bem-Vindo ao RAS - (Robô de Automação de Sistemas)
    
    RAS irá iniciar o processo de automação agora.
    
    Durante o processo não toque no teclado e no mouse,
    ao final no processo você será avisado.
    
    
    RAS 0.1v - Desenvolvido por Matheus L. Marchetti
""")
# Tempo de pausa para carregamento das ações na máquina
pyautogui.PAUSE = 1
# Mudar área de trabalho
time.sleep(1)
pyautogui.hotkey('ctrl', 'winleft', 'right')
time.sleep(1)
# Pesquisar pela aplicação e abir
pyautogui.press('winleft')
pyautogui.write('Aplicativos: SIFAR.exe')
time.sleep(1)
pyautogui.press('backspace')
pyautogui.press('enter')
time.sleep(2)
# Cadastrar usuário
pyautogui.click(708, 399)
pyautogui.write('matheus')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.click(708, 399)
time.sleep(1)
# Entrar com usuário e senha
pyautogui.write('matheus')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.click(591, 381)
# Entrada de dados
with open('../script_de_comandos/comandos.txt', 'r') as arquivo:
    for linha in arquivo:
        agrupamento = linha.split(',')[0]
        sub_agrupamento = linha.split(',')[1]
        data = linha.split(',')[2]

        pyautogui.click(393, 318, duration=1)
        pyautogui.write(agrupamento)

        pyautogui.click(390, 343, duration=1)
        pyautogui.write(sub_agrupamento)

        pyautogui.click(387, 371, duration=1)
        pyautogui.write(data)

        pyautogui.click(314, 525, duration=1)
        time.sleep(1)
pyautogui.click(378, 525)
# Mensagem de finalização do processo de automação
pyautogui.alert("""
    Processo de automação concluído!
    
    Obrigado por utilizar o RAS.
""")
