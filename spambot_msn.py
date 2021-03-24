'''
    Description:
    Send messages from python to messenger.

    Author: AlejandroV
    Video: https://youtu.be/QQb8GbHGMUw
'''
import pyautogui, webbrowser, datetime
from time import sleep

# default variables
flag = 1

# ids person target
id = 'ID_DESTINATION_HERE'

# hour to be sended
hour_to_send = '12:00'

def send():
    # open messenger
    webbrowser.open(f'https://www.messenger.com/t/{id}')

    # wait 5 seconds
    sleep(5)

    # send message
    pyautogui.typewrite("Este es un mensaje")
    pyautogui.press("enter")
    return 0

# cycle
while flag:
    # hour actual
    hour = datetime.datetime.now().strftime('%I:%M')
    if hour == hour_to_send:
        # send message and finish the program
        flag = send()