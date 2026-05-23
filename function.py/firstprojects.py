# Project 1: Temperature Converter Functions
# Description:
# Write two functions: one to convert Celsius to Fahrenheit, another to convert Fahrenheit to Celsius. Then write a main program that asks the user which conversion they want and calls the appropriate function.
# Requirements:
# · celsius_to_fahrenheit(celsius) – takes a Celsius temperature, returns Fahrenheit ((celsius * 9/5) + 32).
# · fahrenheit_to_celsius(fahrenheit) – takes Fahrenheit, returns Celsius ((fahrenheit - 32) * 5/9).
# · main() – shows menu, gets input, calls the right function, prints result.

# def c_to_f(t):
#     return t*9/5+32
# def f_to_c(t):
#     return (t-32)*5/9
# def main():
#         while True:
#             print('--temp converter--')
#             print('1.c to f')
#             print('2.f to c')
#             print('3.exit')
#             c=input('\nenter choice:')
#             if c=='3':
#                 print('good bye')
#                 break
#             elif c not in ['1','2']:
#                 print('invalid choice')
#             else:
#                 t=float(input('temp:'))
#                 if c=='1':
#                     a=c_to_f(t)
#                     print(f'{t}c = {a:.2f}f')
#                 elif c=='2':
#                     a=f_to_c(t)
#                     print(f'{t}f = {a:.2f}c')
# main()


# Project 2: String Utilities Library
# Description:
# Create a set of small string helper functions. Then write a main program that lets the user choose which utility to use.
# Functions to implement:
# · count_vowels(text) – returns number of vowels (a,e,i,o,u) in the string (case-insensitive).
# · reverse_string(text) – returns the string reversed (using a loop, not slicing).
# · is_palindrome(text) – returns True if text reads the same forwards and backwards (ignore spaces and case).
# · count_words(text) – returns number of words (split by spaces).
# Main program:
# · Show menu (1: Count Vowels, 2: Reverse, 3: Palindrome Check, 4: Word Count, 5: Exit)
# · Ask for a sentence/word, call the function, print result.

# def count_vowels(t:str):
#     c=0
#     for i in t:
#         if i.lower() in 'aeiou':
#             c+=1
#     return c

# def reverse_str(t:str):
#     r=''
#     for i in range(len(t)-1,-1,-1):
#         r=r+t[i]
#     return r

# def is_palindrome(t:str):
#     s=t.replace(' ','').lower()
#     return s==s[::-1]

# def count_words(t):
#     words=t.split()
#     return len(words)
# def main():
#     print('--menu--')
#     print('\n1.count vowels')
#     print('2.reverse')
#     print('3.word count')
#     print('4.palindrome')
#     print('5.exit')
#     while True:
#         c=input('choice:')
#         if c=='5':
#             print('good bye')
#             break
#         elif c not in ['1','2','3','4']:
#             print('invalid choice')
#         else:
#             t=input('enter text:')
#             if c=='1':
#                 print('vowels no:',count_vowels(t))
#             elif c=='2':
#                 print('reverse:',reverse_str(t))
#             elif c=='3':
#                 print('word count:',count_words(t))
#             elif c=='4':
#                 print(is_palindrome(t))
# main()

# Write a function called min_max(numbers) that takes a list
# and returns BOTH the minimum and maximum value.

# def min_max(numbers):
#     return min(numbers),max(numbers)
# smallest, largest = min_max([4, 1, 9, 2, 7])
# print(smallest,largest)

# Functions Are Values
# In Python, functions are objects. You can store them in variables and pass them around.

# def titlecase(text):
#     return text.title()

# def speak(function,text):
#     return function(text)

# t='hello i am sagar and i am learning python'
# print(speak(titlecase,t))

# Write a function called apply_to_all(func, items)
# that applies func to every item in items and returns a new list.
   
# def apply_to_all(func, items):
#     l=[]
#     for i in items:
#         l.append(func(i))
#     return l
# print(apply_to_all(str.upper, ["hello", "world", "python"]))
# print(apply_to_all(len, ["cat", "elephant", "ox"]))





  
  
    







        
    
