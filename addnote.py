import time
context = input('context: ')
note = ''
current_line = ''

print('Enter note, use a . on a line by itself to end.')

while(current_line != '.'):
    current_line = input('\t').strip()
    if (current_line != '.'):
        note += current_line + '\n' 

current_time = time.strftime("%H%M", time.localtime())

print('note added: ' + current_time + '\ncontext: ' + context + '\ndetails: \n' + note)