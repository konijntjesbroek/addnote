#!/usr/bin/python3

import time
from os import path

def main():    
     
    context = get_context()
    note = get_note()

    current_time = time.strftime("%Y-%d-%m-%H%M", time.localtime())

    print(current_time + 
          '\n' + context + 
          '\n' + note
    )
def get_context():
    msg = input('context: ')
    return msg

def get_note():
    note = ''
    current_line = ''
    print('Enter note, use a . on a line by itself to end.')

    while(current_line != '.'):
        current_line = input('\t').strip()
        if (current_line != '.'):
            note += current_line + '\n' 

    return note

if __name__ == '__main__':
    main()