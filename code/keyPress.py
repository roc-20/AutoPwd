import os
import win32con
import win32api
import time
VK_SHIFT = 0x10     # Shift
VK_CONTROL = 0x10   # Control
VK_ESCAPE = 0x1b    # Esc
VK_MENU = 0x12      # Alt
VK_SPACE = 0x20     # Space

class Press(object):
    '''
    Press a Letter: e.g. Press(ord('A')) 
        (Note that letter must be capitalized, lowercase would not be recognized)
    Press a Functional Key: e.g. Press(KeyPress.VK_SHIFT)
    
    Usage: 
        "with Press(VK_SHIFT):" for press down 'Shift' key with other operation
        Or you can use "Press(ord('A')).press().release()" will press 'A' for 0.005 second by default.
    '''
    def __init__(self, key, sleep=0.005) -> None:
        self.key = key
        self.sleep = sleep

    def _press(self):
        win32api.keybd_event(self.key, 0, 0, 0)
        time.sleep(self.sleep)
    
    def _release(self):
        win32api.keybd_event(self.key, 0, win32con.KEYEVENTF_KEYUP, 0)

    def __enter__(self):
        self._press()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._release()

    def press(self):
        self._press()
        return self

    def release(self):
        self._release()


def press_a_letter(ch):
    ch = ord(ch)
    Press(ch).press().release()


def press_shift_with_a_letter(ch):
    with Press(VK_SHIFT):
        ch = ord(ch)
        Press(ch).press().release()
        time.sleep(0.005)


def parse(_str: str):
    '''
    param:
        _str: input parse string
            Support upper/lowercase letters or digits

    return:
        func_list: key press operation for each char
    '''

    func_list = []
    for c in _str:
        if c.isdigit():
            action_func = press_a_letter
            func_list.append(action_func)
        
        elif c.islower():
            lower2upper = lambda c: chr(ord(c)-ord('a')+ord('A'))
            action_func = lambda x: press_a_letter(lower2upper(x))
            func_list.append(action_func)

        elif c.isupper():  
            action_func = press_shift_with_a_letter
            func_list.append(action_func)

    return func_list
