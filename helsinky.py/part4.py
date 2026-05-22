# Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

# An example of expected behaviour:

# line(7, "%")
# line(10, "LOL")
# line(3, "")
# Sample output
# %%%%%%%
# LLLLLLLLLL
# ***

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# a = int(input("num: "))
# b = input("character: ")

# line(a, b)


# Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.

# Some examples of how the function should work:

# box_of_hashes(5)
# print()
# box_of_hashes(2)
# Sample output
##########
##########
##########
##########
##########

##########
##########

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# def box_of_hashes(n):
#     while n>0:
#         line(10,'#')
#         n-=1
# box_of_hashes(5)

# Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Some examples:

# square_of_hashes(5)
# print()
# square_of_hashes(3)
# Sample output
#####
#####
#####
#####
#####

###
###
###

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# def square_of_hashes(n):
#         i=0
#         while i<n:
#              line(n,'#')
#              i+=1
# square_of_hashes(12)

# Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Some examples:

# square(5, "*")
# print()
# square(3, "o")
# Sample output
# *****
# *****
# *****
# *****
# *****

# ooo
# ooo
# ooo

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# def square(n,ch):
#     i=0
#     while i<n:
#         line(n,ch)
#         i+=1
# square(4,'j')

# Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Some examples:

# triangle(6)
# print()
# triangle(3)
# Sample output
#
##
###
####
#####
######

#
##
###

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# def triangle(n):
#     i=1
#     while i<=n:
#         line(i,'#')
#         i+=1
# triangle()

# Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Some examples:

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")
# Sample output
# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****

# o
# oo
# ++
# ++
# ++
# ++

# .
# ..
# ...

# def line(a, b):
#     if b == "":
#         print("*" * a)
#     else:
#         print(b[0] * a)

# def shape(a,b,c,d):
#     i=1
#     while i<=a:
#         line(i,b)
#         i+=1
#     j=1
#     while j<=c:
#         line(a,d)
#         j+=1
# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")

# Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

# Calling spruce(3) should print out

# Sample output
# a spruce!
#   *
#  ***
# *****
#   *
# Calling spruce(5) should print out

# Sample output
# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *
# NB: to the left of the spruce there should be exactly the right amount of whitespace. If the shape of the spruce looks correct, but the left edge of the tree is not touching the left edge of the text area in the terminal, the tests will not accept the solution.

# solution pending

# Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

# An example of how the function is used:

# print(greatest_number(3, 4, 1)) # 4
# print(greatest_number(99, -4, 7)) # 99
# print(greatest_number(0, 0, 0)) # 0

# def greatest_number(a,b,c):
#     return max(a,b,c)
# print(greatest_number(1,2,2))

# Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

# Some examples of how the function is used:

# # same characters m and m
# print(same_chars("programmer", 6, 7)) # True

# # different characters p and r
# print(same_chars("programmer", 0, 4)) # False

# # the second index is not within the string
# print(same_chars("programmer", 0, 12)) # False

# def same_chars(a,b,c):
#     if 0<=b<len(a) and 0<=c<len(a):
#         if a[b]==a[c]:
#             return True
#         else:
#             return False
#     else:
#         return False
# print(print(same_chars("programmer", 6, 7)))
# print(same_chars("programmer", 0, 4))
# print(same_chars("programmer", 0, 12))

# shorter solution
# def same_chars(a, b, c):
#     if 0 <= b < len(a) and 0 <= c < len(a):
#         return a[b] == a[c]
#     return False

# Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

# As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

# sentence = "it was a dark and stormy python"

# print(first_word(sentence)) # it
# print(second_word(sentence)) # was
# print(last_word(sentence)) # python
# Sample output
# it
# was
# python

# sentence = "it was"

# print(second_word(sentence)) # was
# print(last_word(sentence)) # was

# sentence = "it was a dark and stormy python"
# def first_word(sentence):
#     word=sentence.split()
#     return word[0]
# def second_word(sentence):
#     word=sentence.split()
#     return word[1]
# def last_word(sentence):
#     word=sentence.split()
#     return word[-1]
# print(first_word(sentence)) 
# print(second_word(sentence)) 
# print(last_word(sentence)) 

# list

# Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.

# An example execution of the program:

# Sample output
# Index: 0
# New value: 10
# [10, 2, 3, 4, 5]
# Index: 2
# New value: 250
# [10, 2, 250, 4, 5]
# Index: 4
# New value: -45
# [10, 2, 250, 4, -45]
# Index: -1

# l=[1, 2, 3, 4, 5]
# while True:
#     i=int(input('index:'))
#     if i==-1:
#        break
#     v=int(input('new value:'))
#     l[i]=v
#     print(l)

# Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
# The list is printed out in the beginning and after each operation. Have a look at the example execution below:
# Sample output
# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!
# You may assume that, if the list is empty, there will not be an attempt to remove items.

# l=[]
# print(f'The list is now {l}')
# while True:
#     c=input('a(d)d, (r)emove or e(x)it:').lower()
#     if c=='x':
#         print('Bye!')
#         break
#     elif c=='d':
#         if len(l)==0:
#             l.append(1)
#         else:
#             l.append(l[-1]+1)
#         print(f'The list is now {l}')
#     elif c=='r':
#         l.pop()
#         print(f'The list is now {l}')
#     else:
#         print('invalid choice!')

# Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

# l=[]
# while True:
#     w=input('word:')
#     if w in l:
#         print(f'You typed in {len(l)} different words')
#         break
#     else:
#         l.append(w)
        

# Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:
# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.

# l=[]
# while True:
#     n=int(input('New item:'))
#     if n==0:
#         print('bye')
#         break

#     l.append(n)   # else is not needed after break
#     print(f'The list now: {l}')
#     print(f'The list in order: {sorted(l)}')

# Please write a function named length which takes a list as its argument and returns the length of the list.
# my_list = [1, 2, 3, 4, 5]
# result = length(my_list)
# print("The length is", result)
# # the list given as an argument doesn't need to be stored in any variable
# result = length([1, 1, 1, 1])
# print("The length is", result)
# Sample output
# The length is 5
# The length is 4

# def length(l):
#     return len(l)

# listt=[1,2,3,4]
# print(f'The length is {length(listt)}')
    
# Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)
# Sample output
# mean value is 3.0

# def mean(l: list):
#     return sum(l)/len(l)
    
# listt=[1,2,3,4,5]
# result=mean(listt)
# print(f'mean value is {result}')

# Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.
# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)
# Sample output
# The range of the list is 4

# def range_of_list(l:list):
#     return max(l)-min(l)
# listt=[1,2,3,4,5]
# range=range_of_list(listt)
# print(f'The range of the list is {range}')

# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
# Some examples of how the function should work:
# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False

# def anagrams(a:str,b:str):
#     return sorted(a)==sorted(b)
# print(anagrams('sagar','aagsr'))
    
# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.
# Please also write a main program which asks the user to type in words until they type in a palindrome:
# def palindromes(s:str):
#     org=list(s)
#     rev=[]
#     for i in range(len(s)-1,-1,-1):
#         rev.append(s[i])
#     return (org==rev)
# print(palindromes('neveroddoreven'))

# while True:
#     strr=input('Please type in a palindrome:')
#     s=palindromes(strr)
#     if s==True:
#         print(f'{strr} is a palindrome!')
#         break
#     print("that wasn't a palindrome")

# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
# def sum_of_positives(l:list):
#     summ=0
#     for i in l:
#         if i>0:
#             summ+=i
#     return summ
# print(sum_of_positives([1,-1,2,3,-3]))

# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.
# def even_numbers(l:list):
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#     return even 
# print('new list:',even_numbers([12,13,14,15,2,4,]))

# Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.
# def list_sum(l1:list,l2:list):
#     new_list=[]
#     for i in range(len(l1)):
#         new_list.append(l1[i]+l2[i])
#     return new_list
# print(list_sum([1,2,3],[1,2,6]))

# Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
# def distinct_numbers(l):
#     return sorted(set(l))

# Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.
# def length_of_longest(l:list):
#     longest=''
#     for i in l:
#         if len(i)>len(longest):
#             longest=i
#     return len(longest)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = length_of_longest(my_list)
# print(result)
   
# Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.
# The order of the strings in the returned list should be the same as in the original.
# def all_the_longest(l:list):
#     longest=l[0]
#     new=[]
#     for i in l:
#         if len(i)>len(longest):
#             longest=i
#     for j in l:
#         if len(j)==len(longest):
#             new.append(j) # this line adds longest to new list so no extra appending the longest is needed
#     # new.append(longest)
#     return new
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = all_the_longest(my_list)
# print(result) 

# # Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.
# # Hint: use f-strings to format the floating point numbers into suitable strings.
    
# def formatted(l:list):
#     new=[]
#     for i in l:
#         new.append(f'{i:.2f}')
#     return new
# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)
              
# # Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.
# def everything_reversed(l):
#     new=[]
#     for i in range(len(l)-1,-1,-1):
#         new.append(l[i][::-1])
#     return new
# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)

# # Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
# def most_common_character(s:str):
#     most_common=s[0]
#     for i in s:
#         if s.count(i)>s.count(most_common):
#             most_common=i
#     return most_common
# first_string = "abcdbde"
# print(most_common_character(first_string))

# # Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.
# # you can assume the string will contain only characters from the lowercase English alphabet a...z.    

# def no_vowels(s:str):
#     new=''
#     for i in s:
#         if i not in 'aeiou':
#             new+=i
#     return new
# my_string = "this is an example"
# print(no_vowels(my_string))  #ths s n xmpl

# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
# def no_shouting(l:list):
#     new_list=[]
#     for i in l:
#         if not i.isupper():
#             new_list.append(i)
#     return new_list
# my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
# pruned_list = no_shouting(my_list)
# print(pruned_list)

# Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.
# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

# An example function call:

# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))
# Sample output
# 4

# in this exercise you will write a program for printing out grade statistics for a university course.
# The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.
# Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.
# The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.
# And example of how the data is typed in:
# Sample output
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:
# When the user types in an empty line, the program prints out statistics. They are formulated as follows:
# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.
# The grade for the course is determined based on the following table:
# exam points + exercise points	grade
# 0–14	0 (i.e. fail)
# 15–17	1
# 18–20	2
# 21–23	3
# 24–27	4
# 28–30	5
# There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.
# With the example input from above the program would print out the following statistics:
# Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *

# def grade(m:int):  # m=marks
#     if 0<=m<=14:
#         g=0
#     elif 15<=m<=17:
#         g=1
#     elif 18<=m<=20:
#         g=2
#     elif 21<=m<=23:
#         g=3
#     elif 24<=m<=27:
#         g=4
#     elif 28<=m<=30:
#         g=5
#     return g
# total_points=[]
# grades=[]
# c=0
# passed=0
# while True:
#     p=input('Exam points and exercises completed :')
#     if p=='':
#         break
#     c+=1
#     exam_point=int(p.split()[0])
#     excercise_point=int(p.split()[1])//10
#     total_p=exam_point+excercise_point
#     if exam_point<10:
#         grd=0
#     else:
#         grd=grade(total_p)
    
#     if grd>0:
#         passed+=1
#     total_points.append(total_p)
#     grades.append(grd)
# print('Statistics:')
# print(f'Points average: {(sum(total_points)/c):.1f}')
# print(f'Pass percentage: {(passed/c *100):.1f}')
# print('Grade distribution:')
# for i in range(5, -1, -1):
#     stars = '*' * grades.count(i)
#     print(f'{i}: {stars}')
 
       









    
    


    
        
       
    

