# Project 1: Simple Note Saver
# What to build:
# A program that runs in a loop and lets the user:

# Add a note (saved to notes.txt permanently)
# View all saved notes (read from the file and display them numbered)
# Clear all notes (with a confirmation prompt)
# Quit the program
import os
while True:
    print('--menu--')
    print('1. Add note')
    print('2. View notes')
    print('3. Clear notes')
    print('4. Quit')
    c=input("Enter choice: ")
    if c=='1':
        with open('notes.txt','a') as f:
            note=input('enter note:')
            f.write(note+'\n')
    elif c=='2':
        if os.path.exists('notes.txt'):
            with open('notes.txt','r') as f:
                lines=f.readlines()
                if not lines:
                    print('no notes yet')
                else:
                    for i,line in enumerate(lines,start=1):
                        print(f'{i}:{line.strip()}')
    elif c=='3':
        conformation=input('are you sure you want to clear all notes ?(yes/no)').lower()
        if conformation=='yes':
            with open('notes.txt','w') as f:
                pass
        elif conformation=='no':
            print('ok, file notes not cleared')
        else:
            print("Invalid input. Notes not cleared.")
    elif c=='4':
        print('ok quited')
        break
    else:
        print('invalid choice!')

# Project 2: Log File Analyzer
# What to build:
# A program that reads a log file and produces a summary report saved to another file.
# First, create this sample server.log file yourself (just paste it and save):
# 2024-01-15 10:23:45 ERROR Database connection failed
# 2024-01-15 10:24:01 INFO Server started successfully
# 2024-01-15 10:25:12 WARNING High memory usage detected
# 2024-01-15 10:26:00 INFO User login: alice
# 2024-01-15 10:27:33 ERROR Disk write failed
# 2024-01-15 10:28:10 WARNING CPU temperature high
# 2024-01-15 10:29:00 INFO Backup completed
# Your program must:

# Read server.log line by line
# Count how many ERROR, WARNING, and INFO lines exist
# Collect all ERROR lines separately
# Write a clean summary report to log_report.txt showing the counts and listing all errors
# Handle the case where server.log doesn't exist
import os

if os.path.exists('server.log'):
    
    with open('server.log','r') as f:
        d={}
        error=[]
        for line in f:
            if 'ERROR' in line:
                d['ERROR']=d.get('ERROR',0)+1
                error.append(line)
            elif 'WARNING' in line:
                d['WARNING']=d.get('WARNING',0)+1
            elif 'INFO' in line:
                d['INFO']=d.get('INFO',0)+1
    with open('log_report.txt','w') as f2:
        f2.write('--summary report--')
        f2.write(f"\nno of lines containing ERROR:{d.get('ERROR',0)}")
        f2.write(f"\nno of lines containing WARNING:{d.get('WARNING',0)}")
        f2.write(f"\nno of lines containing INFO:{d.get('INFO',0)}")
        f2.write('\nlines containing ERROR:\n')
        for i in error:
            f2.write(i)
   
else:
    print('file does not exists')


        

    