import pyautogui
import keyboard
import time
wait_time = 0.05
def type_out_text(text):
    keyboard.press_and_release("enter")
    time.sleep(wait_time)
    for char in text:
        keyboard.write(char)
        time.sleep(wait_time)
    keyboard.press_and_release("enter")

def focus():
    image_path = "1.png"
    center = pyautogui.locateCenterOnScreen(image_path)
    print(center)
    if center:
        x, y = center
        pyautogui.moveTo(x, y)
        pyautogui.click()

def read_file_id_and_type(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            command = line.replace("\n", "")
            print(command)
            type_out_text(command)
            time.sleep(wait_time*2)

def read_file_and_type(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            command = line.replace("\n", "")
            print(command)
            type_out_text(command)
            time.sleep(wait_time*2)

if __name__ == "__main__":
    file_name = input("input file name: ")
    focus()
    read_file_and_type(file_name)
