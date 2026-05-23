# Project 1: Simple Note Saver
# What to build:
# A program that runs in a loop and lets the user:

# Add a note (saved to notes.txt permanently)
# View all saved notes (read from the file and display them numbered)
# Clear all notes (with a confirmation prompt)
# Quit the program

note=input('enter note:')
with open('notes.txt','w') as f:
    f.wri