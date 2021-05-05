### Definition of Success
Useful program that unobtrusively creates notes in a single repository and allows
me to parse and sync this with my projects.

### Phase 1:
- Read input and validate it 
- Request a context
- Print the note in the following format:
```
YYYY-mm-dd HHMM
Context
Note text
```
### DONE
```
~/widd$ ./addnote.py
context: widd  
Enter note, use a . on a line by itself to end.
    Phase one confirmed complete
    .
2021-05-05-0942
widd
Phase one confirmed complete

~/widd$ 
```
### Phase 2:
- Create a shim to allow replit to run the application. Complete
- Create a document for today's date if one does not exist.
- Append note to note for today's date.

### Phase 3:
- Allow users to configure how and where they want to store their notes.
- Allow users to review and edit notes.

### Phase 4:
- Create new directories for non existing projects.
- Sync notes to projects based on context.
