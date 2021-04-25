import time
from os import path

def main():
    CFG_FILE = "notes.cfg"
    CFG_PATH = ".cfg"

    context = input('context: ')
    note = ''
    current_line = ''

    print('Enter note, use a . on a line by itself to end.')

    while(current_line != '.'):
        current_line = input('\t').strip()
        if (current_line != '.'):
            note += current_line + '\n' 

    current_time = time.strftime("%H%M", time.localtime())

    print('note added: ' + current_time + 
          '\ncontext: ' + context + 
          '\ndetails: \n' + note
    )
def get_config(cfg_file)

if __name__ == '__main__':
    main()