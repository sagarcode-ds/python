# # Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.
# def longest(strings: list):
#     longest_str=''
#     for l in strings:
#         if len(l)>len(longest_str):
#             longest_str=l
#     return longest_str 
# strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
# print(longest(strings))

# Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.
# def count_matching_elements(matrix: list, element: int):
#     c=0
#     for row in matrix:
#         for item in row:
#             if item==element:
#                 c+=1
#     return c
# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))

# In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.
# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:
# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.
# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.

# def who_won(game_board: list):
#     score1 = 0
#     score2 = 0

#     for row in game_board:
#         for cell in row:
#             if cell == 1:
#                 score1 += 1
#             elif cell == 2:
#                 score2 += 1

#     if score1 > score2:
#         return 1
#     elif score2 > score1:
#         return 2
#     return 0

# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.
# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# def row_correct(sudoku: list, row_no: int):
#     row = sudoku[row_no]
#     for num in row:
#         if num != 0 and row.count(num) > 1:
#             return False

#     return True

# # Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single column, as its arguments. Columns are indexed from 0.
# # The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# def column_correct(sudoku: list, column_no: int):
#     l=[]
#     for row in sudoku:
#         l.append(row[column_no])
#     for item in l:
#         if item != 0 and l.count(item)>1:
#             return False
#     return True

# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

# def double_items(numbers: list):
#     new=[]
#     for i in numbers:
#         new.append(2*i)
#     return new
# numbers = [2, 4, 5, 3, 11, -4]
# numbers_doubled = double_items(numbers)
# print("original:",numbers)
# print("doubled:", numbers_doubled)

# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.
# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.
# The function should not have a return value - it should directly modify the list it receives as a parameter.
# def remove_smallest(numbers: list):
#     numbers.remove(min(numbers))
# numbers = [2, 4, 6, 1, 3, 5]
# remove_smallest(numbers)
# print(numbers)

# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.
# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

# def block_correct(sudoku: list, r: int, c: int):
#     l=[]
#     for row in range(r,r+3):
#         for column in range(c,c+3):
#             l.append(sudoku[row][column])
#     for i in l:
#         if i!=0 and l.count(i)>1:
#             return False
#     return True
            
# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.
# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False. 
# def row_correct(sudoku: list, row_no: int):
#     row = sudoku[row_no]
#     for num in row:
#         if num != 0 and row.count(num) > 1:
#             return False
#     return True
# def column_correct(sudoku: list, column_no: int):
#     l=[]
#     for row in sudoku:
#         l.append(row[column_no])
#     for item in l:
#         if item != 0 and l.count(item)>1:
#             return False
#     return True
# def block_correct(sudoku: list, row_no: int, column_no: int):
#     l=[]
#     for row in range(row_no,row_no+3):
#         for column in range(column_no,column_no+3):
#             l.append(sudoku[row][column])
#     for i in l:
#         if i!=0 and l.count(i)>1:
#             return False
#     return True
                      
        
# def sudoku_grid_correct(sudoku: list):
#     for i in range(9):
#         if row_correct(sudoku,i)==False:
#             return False
#     for j in range(9):
#         if column_correct(sudoku, j)==False:
#             return False
#     for r in [0, 3, 6]:
#         for c in [0, 3, 6]:
#             if block_correct(sudoku, r,c)==False:
#                 return False
#     return True

# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# print_sudoku(sudoku)
# add_number(sudoku, 0, 0, 2)
# add_number(sudoku, 1, 2, 7)
# add_number(sudoku, 5, 7, 3)
# print()
# print("Three numbers added:")
# print()
# print_sudoku(sudoku)
# Sample output
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Three numbers added:

# 2 _ _  _ _ _  _ _ _
# _ _ 7  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ 3 _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# def print_sudoku(sudoku: list):
#     for i in range(len(sudoku)):
#         for j in range(len(sudoku[i])):
#             if sudoku[i][j]==0:
#                 print('_',end='')
#             else:
#                 print(sudoku[i][j],end='')
#             # spacing
#             if j%3==2 and j!=len(sudoku[i])-1:
#                 print('  ',end='')
#             elif j!=len(sudoku[i])-1:
#                 print(' ',end='')
#             else:
#                 print('',end='')
#         print()
#         if i%3==2 and i!=len(sudoku)-1:
#             print()
# s  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# # print_sudoku(s)

# def add_number(sudoku: list, row_no: int, column_no: int, number:int):
#     sudoku[row_no][column_no]=number   
# add_number(s,2,4,5)

# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.
# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.
# The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:
# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)
# Sample output
# Original:
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Copy:
# 2 _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _     

# def print_sudoku(sudoku: list):
#     for i in range(len(sudoku)):
#         for j in range(len(sudoku[i])):
#             if sudoku[i][j]==0:
#                 print('_',end='')
#             else:
#                 print(sudoku[i][j],end='')
#             # spacing
#             if j%3==2 and j!=len(sudoku[i])-1:
#                 print('  ',end='')
#             elif j!=len(sudoku[i])-1:
#                 print(' ',end='')
#         print()
#         if i%3==2 and i!=len(sudoku)-1:
#             print()

# def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#     copy = []
#     for row in sudoku:
#         copy.append(row[:])
#     copy[row_no][column_no]=number
#     return copy

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print("\nCopy:")
# print_sudoku(grid_copy)

# Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.
# Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.
# NB: when compared to the sudoku exercises, the arguments the function takes are the other way around here. The column x comes first, and the row y second.
# The board consists of the following strings:
# "": empty square
# "X": player 1 symbol
# "O": player 2 symbol
# The function should return True if the square was empty and the symbol was successfully placed on the game board. The function should return False if the square was occupied, or if the coordinates weren't valid.
# An example execution of the function:
# game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
# print(play_turn(game_board, 2, 0, "X"))
# print(game_board)
# Sample output
# True
# [['', '', 'X'], ['', '', ''], ['', '', '']]

# def play_turn(game_board: list, x: int, y: int, piece: str):
#     if y>=len(game_board) or x>=len(game_board[y]) or x<0 or y<0:
#         return False
#     if game_board[y][x]!="":
#         return False

#     game_board[y][x]=piece
#     return True
     
    
# game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
# print(play_turn(game_board, 2, 0, "X"))
# print(game_board)

# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.
# The following matrix
# 1 2 3
# 4 5 6
# 7 8 9
# transposed looks like this:
# 1 4 7
# 2 5 8
# 3 6 9
# The function should not have a return value. The matrix should be modified directly through the reference.

# def transpose(matrix: list):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if j>i:
#                 matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(transpose(matrix))

# dictionary

# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive
# The value mapped to each key should be the key times ten.
# For example:
# d = times_ten(3, 6)
# print(d)
# Sample output
# {3: 30, 4: 40, 5: 50, 6: 60}

# def times_ten(start_index: int, end_index: int):
#     d={}
#     for i in range(start_index, end_index+1):
#         d[i]=i*10
#     return d
# d = times_ten(3, 6)
# print(d)

# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.
# def factorials(n: int):
#     d={}
    
#     for i in range(1,n+1):
#         f=1
#         for j in range(1,i+1):
#             f=f*j
        
#         d[i]=f
#     return d
# print(factorials(5),type(factorials(5)))
# k=factorials(5)
# print(k[4])
    
# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.
# For example, the function call histogram("abba") should print out
# Sample output
# a **
# b **
# while histogram("statistically") should print out
# Sample output
# s **
# t ***
# a **
# i **
# c *
# l **
# y *

# def histogram(s):
#     d={}
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     for j in d:
#         print(f"{j} {'*'*d[j]}")
# histogram('statistically')

# Please write a phone book application. It should work as follows:
# Sample output
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

# As you can see above, each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

# phone_book={}
# while True:
#     c=input('command (1 search, 2 add, 3 quit):')
#     if c=='3':
#         print('quitting...')
#         break
#     elif c not in ['1','2']:
#         print('invalid choice! try again')
#     else:
#         name=input('name:')
#         if c=='1':
#             if name in phone_book:
#                 print(phone_book[name])
#             else:
#                 print('no number')
#         elif c=='2':
#             number=input('number:')
#             phone_book[name]=number
#             print('ok!')

# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...


# phone_book={}
# while True:
#     c=input('command (1 search, 2 add, 3 quit):')
#     if c=='3':
#         print('quitting...')
#         break
#     elif c not in ['1','2']:
#         print('invalid choice! try again')
#     else:
#         if c=='1':
#             name=input('name:')
#             if name in phone_book:
#                 for i in (phone_book[name]):
#                      print(i)
#             else:
#                 print('no number')
#         elif c=='2':
#             name=input('name:')
#             no=input('number:')
#             if name in phone_book:
#                 phone_book[name].append(no)
#             else:
#                 phone_book[name]=[no]
#             print('ok!')
# # print(type(phone_book[name]))
# print(phone_book)
            
# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.
# def invert(dic: dict):
#     items=list(dic.items())
#     dic.clear()
#     for k,v in items:
#         dic[v]=k
# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# print(invert(s))
# print(s)

# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. Please have a look at the example below:
# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
# Sample output
# two
# eleven
# forty-five
# ninety-nine
# zero
# NB: Please don't formulate each spelled out number by hand. Figure out how you can use loops and dictionaries in your solution.
# d1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
# d2 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
# def dict_of_numbers():
#     d={}
#     for i in range(100):
#         if 0<=i<=19:
#             d[i]=d1[i]
#         elif i%10==0:
#             d[i]=d2[i]
#         else:
#              f=str(i)[0]
#              l=str(i)[1]
#              d[i]=d2[int(f)*10]+'-'+ d1[int(l)]
#     return d
# n=dict_of_numbers()
# print(n[99])

# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.
# # The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.
# name
# director
# year
# runtime
# The values attached to these keys are given as arguments to the function.
# An example of its use:
# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)
# Sample output
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
# def add_movie(database: list, name: str, director: str, year: int, runtime: int):
#     database.append({
#         "name": name,
#         "director": director,
#         "year": year,
        # "runtime": runtime
#     })
# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)

# # Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.
# def find_movies(database: list, search_term: str):
#     new=[]
#     for i in database:
#         if search_term.lower() in i['name'].lower():
#             new.append(i)
#     return new
            
    

# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

# my_movies = find_movies(database, "python")
# print(my_movies)
# # print(database[0]['name']) #Gone with the Python

#  Tuple
# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:
# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments
    
# def create_tuple(x: int, y: int, z: int):
#     return (min(x,y,z),max(x,y,z),x+y+z)
# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))

# # Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.
# def oldest_person(people: list):
#     oldest=people[0][0]
#     year=people[0][1]
#     for person in people:
#         if person[1]<year:
#             year=person[1]
#             oldest=person[0]
#     return oldest
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))

# In this exercise we are handling tuples just like the ones described in the previous exercise.
# Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.

# def older_people(people: list, year: int):
#     new=[]
#     for person in people:
#         if person[1]<year:
#             new.append(person[0])
#     return new
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)

