import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() #Pega o tamanho do monitor principal
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position() #Pega as posições X e Y do mouse
print(currentMouseX, currentMouseY)

currentMouseX, currentMouseY = 15, 1065
print(currentMouseX, currentMouseY)

pyautogui.moveTo(currentMouseX, currentMouseY)
time.sleep(2)

pyautogui.click()