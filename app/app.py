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
pyautogui.write('app.exe')
pyautogui.press('backspace')
pyautogui.press('enter')
time.sleep(2)
# Mensagem de finalização do processo de automação
pyautogui.alert("""
    Processo de automação concluído!
    
    Obrigado por utilizar o RAS.
""")