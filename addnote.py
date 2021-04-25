import time
context = input('context: ')
note = ''
current_line = ''

print('Enter note, use a . on a line by itself to end.\n')

while(current_line != '.'):
    current_line = input('\t').strip()
    if (current_line != '.'):
        note += current_line + '\n' 

print('Context: ' + context + '\nNote:\n\n' +note)