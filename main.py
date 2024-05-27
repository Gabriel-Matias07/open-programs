import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() #Pega o tamanho do monitor principal
print(screenWidth, screenHeight)

# currentMouseX, currentMouseY = pyautogui.position() #Pega as posições X e Y do mouse
# print(currentMouseX, currentMouseY)

# currentMouseX, currentMouseY = 18, 1079
# print(currentMouseX, currentMouseY)

# pyautogui.moveTo(currentMouseX, currentMouseY)
# time.sleep(2)

#Discord:
pyautogui.press('win')
time.sleep(1)
pyautogui.write('Discord', interval=0.25)
pyautogui.press('enter')
time.sleep(2)

#Google Chrome
pyautogui.press('win')
time.sleep(1)
pyautogui.write('Google Chrome', interval=0.24)
pyautogui.press('enter')
time.sleep(1)

currentMouseX, currentMouseY = 865, 610
pyautogui.click(currentMouseX, currentMouseY)