# Project 1: Countdown Timer
# Topics: while loop, user input, arithmetic
# Write a program that:
# 1. Asks the user for a starting number (e.g., 10).
# 2. Prints numbers from that number down to 1, each on a new line.
# 3. After the countdown, prints "Blast off!".

# n=int(input('enter a number:'))
# while n>0:
#     print(n)
#     n-=1
# print('Blast off!')

# Project 2: Password Guessing Game
# Topics: while loop, conditionals, string comparison
# Set a fixed password (e.g., "python"). The user has 3 attempts to guess it.
# · After each wrong guess, tell them how many attempts are left.
# · If they guess correctly, print "Access granted" and stop.
# · If they run out of attempts, print "Access denied".

# p1='sagar@10'
# a=3   # attempt
# while True:
#     p2=input('enter password:')
#     a-=1
#     if p2==p1:
#         print('access granted')
#         break
#     else:
#         if a>0:
#             print(f'wrong password!,{a} attempts are left')
#         elif a==0:
#             print('access denied!')
#             break

# Project 3: Sum of Positive Numbers
# Topics: while loop, user input, accumulation
# Ask the user to enter numbers repeatedly. Stop when they enter 0. Then print the sum of all positive numbers entered (ignore negative numbers, but still count them? Actually just sum positives). Also print how many positive numbers were entered.
 
# c=0  
# s=0
# cp=0
# while True:
#     n=int(input('enter a num,(0 to stop):'))
#     c+=1
#     if n>0:
#         s=s+n
#         cp+=1
#     elif n==0:
#         break
# print('sum of positives:',s)
# print('counts of num:',c)
# print('counts of positives:',cp)

# Project 4: Multiplication Practice
# Topics: while loop, arithmetic, user input
# Generate two random numbers? But you can't use import random. Instead, fix two numbers (e.g., first number from 2 to 5, second from 3 to 6) but better: let the user choose a table. Actually simpler: Ask the user for a number (e.g., 7), then print its multiplication table from 1 to 10 using a while loop.

# n=int(input('enter a num:'))
# i=1
# while i<=10:
#     print(f'{n}*{i}={n*i}')
#     i+=1

# Project 5: Average Calculator (Unknown Count)
# Topics: while loop, accumulation, averaging
# Ask the user to enter numbers. Stop when they enter -1. Then print the average of all numbers entered (excluding the -1). If no numbers were entered, print "No numbers entered".

# s=0
# c=0
# while True:
#     n=int(input('enter a num:'))
#     if n==-1:
#         break
#     elif n != -1:
#         s=s+n
#         c+=1
# if c>0:
#     print('average:',s/c)
# else:
#     print('no numbers entered')

# Project 6: Reverse a Number
# Topics: while loop, arithmetic (no modulo – alternative approach using string conversion)
# Ask the user for a positive integer. Print its digits in reverse order. Do not use modulo (%). Instead, convert the number to a string, then use string indexing with a while loop.
    
# n=int(input('enter a num:'))
# n=str(n)
# i=len(n)-1
# while i>=0:
#     print(n[i],end='')
#     i-=1

# Project 7: Simple Menu with While Loop
# Topics: while loop, conditionals, dictionary (optional)
# Create a menu for a small calculator. Options:
# 1. Add two numbers
# 2. Subtract two numbers
# 3. Multiply two numbers
# 4. Exit
# The program should keep showing the menu until the user chooses exit. For options 1-3, ask for two numbers, perform the operation, print the result, then show menu again.

# menu={
#     '1':'add',
#     '2':'substract',
#     '3':'multiply',
#     '4':'exit'
# }
# print('Menu:',menu)
# while True:
#     c=input('choice:')
#     if c=='4':
#         print('Goodbye!')
#         break
#     elif c in ['1','2','3']:
#         n1=int(input('enter first num:'))
#         n2=int(input('enter second num:'))
#         if c=='1':
#             result=n1+n2
#         elif c=='2':
#             result=n1-n2
#         elif c=='3':
#             result=n1*n2
        
#         print('result:',result)
#     else:
#         print('invalid choice')
    
# Bonus: Guess the Number (Without Random)
# Topics: while loop, binary search style? No random. Instead, set a fixed secret number (e.g., 42). User guesses until correct. Give hints "too high" or "too low". Count attempts.

# print("I'm thinking of a number between 1 and 100.")
# s=42
# c=0
# while True :
#     n=int(input('Guess :'))
#     c+=1
#     if n==s:
#         print(f'correct you only took {c} attempts.')
#         break
#     elif n>s:
#         print('too high')
#     elif n<s:
#         print('too low')









