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

def item_range_id(start, end, amount=1):
    for i in range(start, end+1):
        command = "@item "+ str(i) + " " + str(amount)
        print(command)
        type_out_text(command)
        time.sleep(wait_time*2)
        
if __name__ == "__main__":
    focus()
    start = input("please input the start id: ")
    end = input("please enter the end id: ")
    amount = input("please enter the item amount: ")
    item_range_id(start, end, amount)
