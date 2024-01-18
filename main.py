comments = []#your comments

links = [ ]#your links

import random
import time

import pyautogui
import requests
from PIL import ImageGrab
from bs4 import BeautifulSoup

selected_comments = []


def move_mouse():
    while True:
        i = 0
        try:
            while i != 15:
                x = random.randint(-100, 100)
                y = random.randint(-100, 100)

                pyautogui.moveRel(x, y, duration=10)

                # Добавим случайные паузы
                pyautogui.click()  # Добавляем клик
                pyautogui.sleep(random.randint(1, 5))
                i += 1
        except KeyboardInterrupt:
            break


def choose_random_comment():
    if len(selected_comments) == 25:
        selected_comments.clear()  # Очищаем список, если он достиг 25 элементов
    comment = random.choice(comments)
    if comment in selected_comments:
        choose_random_comment()
    else:
        selected_comments.append(comment)
    return comment


def check_color():
    x, y = pyautogui.position()
    screenshot = ImageGrab.grab(bbox=(x - 1, y - 1, x + 1, y + 1))

    # Проверяем цвет пикселя под указателем мыши
    pixel_color = screenshot.getpixel((1, 1))

    # Желаемый цвет в формате (R, G, B)
    desired_color = (247, 82, 95)  # Замените на желаемый цвет

    # Сравниваем цвет пикселя с желаемым цветом
    if pixel_color != desired_color:
        return True
    else:
        return False


'''Условие выполнения работы программы - заранее открытый в полноэкранном режиме браузер'''

time.sleep(5)  # ожидение перед началом выполнения программы


# here we need to create an empty list in which we will store links of every post
def link_extracting(link):
    response = requests.get(link)
    comment_links = []

    if response.status_code != 200:
        print(f'Соединение с {link} не установлено')
        return []  # Return an empty list if the connection fails

    html_page = response.text
    soup = BeautifulSoup(html_page, "html.parser")

    for div in soup.find_all("div", class_="tv-widget-idea__title-row"):
        a_tag = div.find("a")
        if a_tag:
            href = a_tag.get("href")
            comment_links.append(href)

    return comment_links


# Create an empty list to store all extracted links
all_links = []

# Iterate through each profile link and extract links, then append them to the 'all_links' list
for link in links:
    all_links.extend(link_extracting(link))
pyautogui.hotkey('alt', 'tab')

for link in all_links:
    pyautogui.moveTo(952, 52, duration=7 )
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write('https://www.tradingview.com' + link)
    pyautogui.press('enter')
    pyautogui.moveTo(1407, 986, duration=7)
    if check_color() is True:
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('comments')
        pyautogui.moveTo(680,623, duration=7)
        pyautogui.click()
        pyautogui.write(choose_random_comment())
        pyautogui.moveTo(1443,698, duration=7)
        pyautogui.click()
    else:
        continue
