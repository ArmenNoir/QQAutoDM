# -*- coding:utf-8 -*-

import win32gui
import win32api
import win32con
import win32clipboard as w
from datetime import datetime, timedelta
from time import sleep
import pause

def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def front_layer(handle):
    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    sleep(2)
    win32gui.SetWindowPos(handle,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
    sleep(2)

def copy_text(message):
    """
    Input message to clipboard
    """
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, message)
    w.CloseClipboard()

def send_msg(handle):
    #hotkey ctrl+enter must change default hotkey
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    now_time = datetime.now()
    print("Sent : ",now_time)

if __name__ == '__main__':
    #get config 
    config = {
    "user": "test",
    "msg": "你好",
    "clock": "2033-05-30 18~00"
    }
    name = config['user']
    msg = config['msg']
    clock = config['clock']

    #Get window by name
    HWND = win32gui.FindWindow(None, name)

    #set 1st layer
    front_layer(HWND)
    #Get input box position 
    rect = win32gui.GetWindowRect(HWND)
    mouse_click(rect[0]+20, rect[3]-70)
    win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
    #copy and paste
    copy_text(msg)
    win32gui.SendMessage(HWND, win32con.WM_PASTE , 0, 0)
    print(msg)
    
    #clock
    if '~' in clock:
        set_time = clock
        auto_time = set_time #'2012-05-29 19~30'
        auto_time += '~00.000000'
    else: #don't set minute or hour -> 10 seconds after run the program
        print('You have not set the time!\nProgram will run after 10s for test')
        now_time = datetime.now() #.strftime('%H:%M:%S')
        set_time = now_time + timedelta(seconds=10)
        set_time = set_time.strftime("%Y-%m-%d %H~%M~%S")#string
        auto_time = set_time #'2012-05-29 19:30:03'
        auto_time += '.000000'
    
    auto_time = datetime.strptime(auto_time, "%Y-%m-%d %H~%M~%S.%f")

    pause.until(auto_time)
    send_msg(HWND)
