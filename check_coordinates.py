import pyautogui
import time


pyautogui.hotkey('alt','tab')
time.sleep(5)
# Получение координат текущего положения указателя мыши
x, y = pyautogui.position()

# Получение цвета пикселя под указателем мыши
pixel_color = pyautogui.pixel(x, y)

print(f"Цвет пикселя на координатах ({x}, {y}): {pixel_color}")
