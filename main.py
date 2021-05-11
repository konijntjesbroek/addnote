#!/usr/bin/python3

import addnote
import revnote
import syncnote

def main():
    menu =  '1 - add note \n2 - review notes\n3 - synchronize notes\n' 
    prompt = 'Please enter a menu selection [1-3]: '
    
    app = ''
    print(menu)
    while not app:
        try:
            app = int(input(prompt).strip())
        except ValueError:
            pass
        else:
            if app < 1 or app > 3:
                app = ''
    if app == 1:
        addnote.main()
    elif app == 2:
        revnote.main()
    elif app == 3:
        syncnote.main()
    else:
        print('Abandon hope, all ye who enter here.')
    

if __name__ == '__main__':
    main()