import keyboard
import random
import time
from pyautogui import press, typewrite

def print_func():
    keyboard.press_and_release('y')
    print('working')
    time.sleep(0.2)
    typewrite(output_word())
    time.sleep(0.1)
    press('\n')
    return 0

def output_word():
    try:
        strings = open("list.txt","r")
        data = strings.read()
        strings_list = data.split('\n')
    except:
        print("Your file broke")
        exit(1)

    ad_out = strings_list[random.randint(0, len(strings_list))]
    print(ad_out)
    return ad_out

def main_loop():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("F4"):  # if key 'q' is pressed
                print_func()
                time.sleep(0.2)
            if keyboard.is_pressed("F5"):
                print('Program Closing')
                break
        except:
            print('Error: Loop Restart')
            break  # if user pressed a key other than the given key the loop will break
    return 0

if __name__ == '__main__':
    main_loop()
    while True:
        print("Minor Error: Restart Program? (F4:Yes F5:No)")
        if keyboard.is_pressed("F4"):  # if key 'q' is pressed
            main_loop()
        if keyboard.is_pressed("F5"):
            print('Program Closed')
            break
