import string
import time
from pip import main
import keyPress as kp
import keyboard


def init():
    with open('./pwd/pwd.txt', 'r') as f:
        pwstr = f.read()

    func_ls = kp.parse(pwstr)
    ch_ls = list(pwstr)
    return pwstr, func_ls, ch_ls


def action(pwstr, func_ls, ch_ls):
    time.sleep(0.15)
    for func, char in zip(func_ls, ch_ls):
        func(char)


def main():
    '''
    Support upper/lowercase letters or digits, insure you are in English input method
    '''
    init_tuple = init()
    while True:
        ''' Input hot key: ctrl+F10 ''' 
        keyboard.add_hotkey('ctrl+f10', action, args=[*init_tuple])
        keyboard.wait()


if __name__ == '__main__':
    main()
