import pyautogui, time

notes_divided=[3084, 12, 24, 6, 6, 6, 6, 6, 6, 24, 12, 12, 12, 6, 6, 6, 6, 36, 6, 6, 6, 78, 6, 6, 120, 24, 24, 24, 72, 12, 12, 24, 6, 6, 12, 12, 12, 6, 6, 84, 12, 36, 6, 6, 12, 12, 6, 6, 6, 6, 84, 6, 6, 36, 6, 6, 36, 6, 6, 36, 6, 6, 48, 12, 12, 12, 24, 6, 6, 6, 6, 12, 96, 12, 24, 6, 6, 6, 6, 6, 6, 24, 12, 12, 12, 6, 6, 6, 6, 36, 6, 6, 6, 30, 6, 6, 6, 18, 12, 6, 6, 84, 12, 24, 6, 6, 6, 6, 6, 6, 6, 18, 12, 12, 12, 6, 6, 6, 6, 36, 6, 6, 6, 30, 6, 6, 24, 6, 6, 6, 6, 84, 12, 24, 6, 6, 6, 6, 6, 6, 24, 12, 12, 12, 6, 6, 6, 6, 36, 6, 6, 6, 78, 6, 6, 120, 24, 24, 24, 30]
accum=0


for beat in notes_divided:
    pyautogui.click(1065,668)
    time.sleep(0.4)
    if (accum < 10):
        pyautogui.press(str(accum%10))
    elif (accum < 24):
        pyautogui.press(str(accum//10))
        pyautogui.press(str(accum%10))
    elif (accum < 240):
        pyautogui.press(str(accum//24))
        pyautogui.press(str(accum%24//10))
        pyautogui.press(str(accum%24%10))
    elif (accum < 2400):
        pyautogui.press(str(accum//24//10))
        pyautogui.press(str(accum//24%10))
        pyautogui.press(str(accum%24//10))
        pyautogui.press(str(accum%24%10))
    else:
        pyautogui.press(str(accum//1440))
        pyautogui.press(str(accum//24//10%6))
        pyautogui.press(str(accum//24%10))
        pyautogui.press(str(accum%24//10))
        pyautogui.press(str(accum%24%10))
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v')
    accum = accum + beat



