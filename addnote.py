#!/usr/bin/python3

import time
from os import path

class Note:
    '''
        The Note class, the core of widd this defines the object components and
        methods for interacting with the note. 
    '''
    def __init__(self, tstamp):
        self.context = ''
        self.text = ''
        self.tstamp = tstamp

    def __str__(self):
        return self.tstamp + '\n' + \
               self.context + '\n' + \
               self.text + '\n\n'

    def get_time(self):
        return self.tstamp

    def set_context(self):
        self.context = input('context: ')
        return

    def get_context(self):
        return self.context

    def set_text(self):
        self.text = ''
        current_line = ''
        print('Enter note, use a . on a line by itself to end.')

        while(current_line != '.'):
            current_line = input('\t').strip()
            if (current_line != '.'):
                self.text += current_line + '\n' 
        return 
    
    def get_note(self):
        return self.text
    
  
def main():    

    current_time = time.strftime("%Y-%m-%d-%H%M", time.localtime())
    filename = current_time[:10] + '.txt'
    
    note = Note(current_time)
    note.set_context()
    note.set_text()

    write_out(str(note), filename)


def write_out(n, f):
    print(f'printing to {f}\n{n}')

    with open(f, 'w') as ofile:
        ofile.write(n)

if __name__ == '__main__':
    main()