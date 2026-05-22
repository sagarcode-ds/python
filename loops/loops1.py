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

# Project A: Vowel and Consonant Counter
# Topics: while loop, strings, indexing, conditionals, .lower()
# Ask the user for a sentence. Count how many vowels (a, e, i, o, u) and consonants (letters that are not vowels) it contains. Ignore spaces, digits, and punctuation. Use a while loop to go through each character.

# s=input('enter a sentence :').lower()
# c=0
# v=0
# i=0
# while i<len(s):
#     letter=s[i]
#     if 'a'<=letter<='z':
#         if letter in 'aeiou':
#             v+=1
#         else:
#             c+=1
#     i+=1
# print('no of vowels:',c)
# print('no of consonants:',c)

# Project B: Word Reverser (Reverse Order of Words)
# Topics: while loop, string methods (.split()), list indexing, concatenation
# Ask the user for a sentence. Print the sentence with words in reverse order, but each word spelled normally. Use .split() to get a list of words, then use a while loop to build the reversed sentence.

# s=input('enter a sentence :')
# words=s.split()
# print(words)
# i=len(words)-1
# reversed=''
# while i>=0:
#     if len(reversed)==0:
#         reversed=words[i]
#     else:
#         reversed=reversed+ ' '+words[i]

#     i-=1
# print(reversed)
    
# Project C: Phonebook Menu (Dictionary)
# Topics: while loop, dictionary, user input, conditionals
# Create a phonebook using a dictionary. Show a menu:
# 1. Add contact (name and phone number)
# 2. Search contact (by name)
# 3. Delete contact
# 4. Show all contacts
# 5. Exit
# contacts={'sagar':'9767631946','alice':'9847133427'}

# while True:
#     print('\n-----phonebook-----')
#     print('1:add','2:search','3:delete','4:show all','5:exit')

#     c=input('choice :')
#     if c=='1':
#         add_name=input('name of contact:')
#         add_no=input('phone no :')
#         contacts.update({add_name:add_no})
#         print(contacts)
#     elif c=='2':
#         search_contact=input('enter name to search :')
#         if search_contact in contacts:
#             print('contact:',search_contact,':',contacts[search_contact])
#         else:
#             print(f'{search_contact} not found!')
#     elif c=='3':
#         del_contact=input('enter contact name to delete:')
#         if del_contact in contacts:
#              del contacts[del_contact]
#         else:
#             print('contact not found')

       
#     elif c=='4':
#         print(contacts)
#     elif c=='5':
#         print('goodbye')
#         break
#     else:
#         print('invalid choice')

# Project D: Remove Duplicate Words from a Sentence (Using Set)
# Topics: while loop, set, .split(), string methods
# Ask the user for a sentence. Remove duplicate words while preserving the order of first appearance. Use a set to track seen words, and a while loop to build a new list of unique words.

# s=input('enter a sentence :',)
# seen=set()
# unique=[]
# words=s.split()
# i=0
# while i<len(words):
#     if words[i] not in seen:
#         seen.add(words[i])
#         unique.append(words[i])
#         # print(i, len(words))
#     i+=1
# print(unique)
# new_sent=''
# j=0
# while j<len(unique):
#     if j==0:
#         new_sent=unique[j]
#     else:
#         new_sent=new_sent+' '+unique[j]
#     j+=1
# print('unique:',new_sent)
    
# Project E: Character Frequency Dictionary (Without Counter)
# Topics: while loop, dictionary, strings
# Ask the user for a word. Create a dictionary that counts how many times each letter appears (case‑insensitive, ignore non‑letters). Use a while loop to iterate through the

# w=input('word:')
# i=0
# freq={}
# while i<len(w):
#     char=w[i]
#     if 'a'<=char<='z':
#         freq[char]=freq.get(char,0)+1
#     i+=1
# print(freq)    

# Project F: Find the Longest Word in a Sentence
# Topics: while loop, list, string methods, comparison
# Ask the user for a sentence. Find and print the longest word. If there is a tie, print the first o

# s=input('sentence :')
# w=s.split()
# # print(w,type(w),len(w))  # debug
# i=0
# longest=''
# # print(type(len(longest))) # debug
# while i<len(w):
#     if len(w[i])>len(longest):
#         longest=w[i]
#     i+=1
# print('longest word:',longest)

# Project G: Palindrome Checker (Ignore Spaces and Case)
# Topics: while loop, string manipulation, conditionals
# Ask the user for a phrase. Check if it is a palindrome (reads the same forwards and backwards), ignoring spaces and case. For example, "A man a plan a canal panama" is a palindrome.

# s=input('phrase:').lower()
# s = ''.join(s.split())
# # print(s)   # debug
# new=''
# i=len(s)-1
# while i>=0:
#         new=new+s[i]
#         i-=1

# # print(new)  #debug
# if s==new:
#     print('palindrome')
# else:
#     print('not palindrome')

# Project M: Substring Search (Without in or find)
# Topics: while loop, string indexing, manual comparison
# Write a program that asks the user for a main string and a substring. Check if the substring appears anywhere inside the main string. You cannot use Python's in operator or .find() / .index() methods. You must manually compare character by character using loops.


    






    
    










