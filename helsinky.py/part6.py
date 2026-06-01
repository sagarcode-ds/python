# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...
# Please write a function named largest, which reads the file and returns the largest number in the file.
# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

# def largest():
#     with open('numbers.txt','r') as f:
#         content=f.read()
#         nums=content.split()
#         new=[]
#         for num in nums:
#             new.append(int(num))
#         return max(new)
# print(largest())

# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:
# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...
# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.
# NB: the function does not take any arguments. The file you are working with is always named fruits.csv.

# def read_fruits():
#     d={}
#     with open('fruits.csv','r') as f:
#         for line in f:
#             line=line.split(';')
#             d[line[0]]=float(line[1].strip())
#         return d
# print(read_fruits())

# The file matrix.txt contains a matrix in the format specified in the example below:
# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as
# 1,2,3
# 2,3,4
# the function should return the list [6, 9].
# def matrix_sum():
#     summ=0
#     with open('matrix.txt') as f:
#         for line in f:
#             line=line.replace('\n','')
#             nums=line.split(',')
#             for i in nums:
#                 summ+=int(i)
#     return summ

# print(matrix_sum())

# def matrix_max():
#     with open('matrix.txt') as f:
#         maxx=0
#         for line in f:
#             nums=line.split(',')
#             for i in nums:
#                 if int(i)>maxx:
#                     maxx=int(i)
#     return maxx
# print(matrix_max())

# def row_sums():
#     with open('matrix.txt') as f:
#         row_sum=[]
#         for line in f:
#             summ=0
#             nums=line.split(',')
#             for i in nums:
#                 summ+=int(i)
#             row_sum.append(summ)
#     return row_sum
# print(row_sums())

# merging 2 files information
# names={}
# with open('employees.csv') as f:
#     for line in f:
#         line=line.strip()
#         parts=line.split(';')
#         if parts[0]=='pic':
#             continue
#         names[parts[0]]=parts[1]
# # print(names)

# salaries={}
# with open('salaries.csv') as f:
#     for line in f:
#         line=line.strip()
#         parts=line.split(';')
#         if parts[0]=='pic':
#             continue
#         salaries[parts[0]]=int(parts[1])
# # print(salaries)

# for pic,name in names.items():
#     print(f"{name:16}:{salaries.get(pic,0)} euros")
    

# This program works with two CSV files. One of them contains information about some students on a course:

# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder
# The other contains the number of exercises each student has completed each week:

# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
# As you can see above, both CSV files also have a header row, which tells you what each column contains.

# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35   

# filename1=input('Student information:')
# filename2=input('Exercises completed: ')
# names={}
# with open(filename1) as f:
#     for line in f:
#         parts=line.strip().split(';')
#         # print(parts)
#         if parts[0]=='id':
#             continue
#         names[parts[0]]=parts[1]+' '+parts[2]
# # print(names)
# excercises={}
# with open(filename2) as f:
#    for line in f:
#       parts=line.strip().split(';')
#       if parts[0]=='id':
#             continue
#       summ=0
#       for i in parts[1:]:
#             summ+=int(i)
#       excercises[parts[0]]=summ
# # print(excercises)
# for id,name in names.items():
#    print(f'{name} {excercises.get(id,0)}')
      
# Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:
# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2
# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.
# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3
# Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.
# The final grade for the course is determined based on the sum of exam and exercise points according to the following table:
# exam points + exercise points	grade
# 0-14	0 (fail)
# 15-17	1
# 18-20	2
# 21-23	3
# 24-27	4
# 28-	5
# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

# def grade(point):
#     if point>=28:
#         grd=5
#     elif point>=24:
#         grd=4
#     elif point>=21:
#         grd=3
#     elif point>=18:
#         grd=2
#     elif point>=15:
#         grd=1
#     else:
#         grd=0
#     return grd

# filename1=  'students.csv' #input('Student information:')
# filename2= 'excercises.csv' #input('Exercises completed:')   
# filename3=  'exam_points.csv'#input('Exam points:')    
# names={}
# with open(filename1) as f:
#     for line in f:
#         parts=line.strip().split(';')
#         if parts[0]=='id':
#             continue
#         names[parts[0]]=parts[1]+' '+parts[2]
# excercises={}

# with open(filename2) as f:
#    for line in f:
#       parts=line.strip().split(';')
#       if parts[0]=='id':
#             continue
#       summ=0
#       for i in parts[1:]:
#             summ+=int(i)
#       e_point=summ//4
#       excercises[parts[0]]=min(e_point,10)
# print('e',excercises)

# grades={}
# with open(filename3) as f:
#     for line in f:
#         parts=line.strip().split(';')
#         if parts[0]=='id':
#             continue
#         summ=0
#         for i in parts[1:]:
#             summ+=int(i)
#         # print(summ)
#         grades[parts[0]]=summ
# print('grd',grades)

# for pic,name in names.items():
#     print(f'{name} {grade(excercises.get(pic,0)+grades.get(pic,0))}')   

# This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
# Each row contains the information for a single student. The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

# def grade(point):
#     if point>=28:
#         grd=5
#     elif point>=24:
#         grd=4
#     elif point>=21:
#         grd=3
#     elif point>=18:
#         grd=2
#     elif point>=15:
#         grd=1
#     else:
#         grd=0
#     return grd

# filename1=input('Student information:')  #'students.csv' 
# filename2=input('Exercises completed:')   # 'excercises.csv' 
# filename3=input('Exam points:')    #  'exam_points.csv'#input('Exam points:')    
# names={}
# with open(filename1) as f:
#     for line in f:
#         parts=line.strip().split(';')
#         if parts[0]=='id':
#             continue
#         names[parts[0]]=parts[1]+' '+parts[2]
# # print('n',names)
# excercises={}
# ex_no={}
# with open(filename2) as f:
#    for line in f:
#       parts=line.strip().split(';')
#       if parts[0]=='id':
#             continue
#       summ=0
#       for i in parts[1:]:
#             summ+=int(i)
#       ex_no[parts[0]]=summ  
#       e_point=summ//4
#       excercises[parts[0]]=min(e_point,10)
# # print('e',excercises)
# # print('e2',ex_no)
# exam_pts={}
# with open(filename3) as f:
#     for line in f:
#         parts=line.strip().split(';')
#         if parts[0]=='id':
#             continue
#         summ=0
#         for i in parts[1:]:
#             summ+=int(i)
#         # print(summ)
#         exam_pts[parts[0]]=summ
        
# # print('exam points',exam_pts)

# print(f"{'name':30} {'exec_nbr':>10} {'exec_pts.':>10} {'exm_pts.':>10} {'tot_pts.':>10} {'grade':>10}")
# for pic,name in names.items():
#     print(f"{names:30} {ex_no[pic]:10} {excercises[pic]:10} {exam_pts[pic]:10} {(excercises[pic]+exam_pts[pic]):10} {(grade(excercises[pic]+exam_pts[pic])):10}")

# Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:
# Sample output
# Write text: We use ptython to make a spell checker
# We use *ptython* to make a spell checker
# Sample output
# Write text: This is acually a good and usefull program
# This is *acually* good and *usefull* program
# The case of the letters should be irrelevant to the functioning of your program.
# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

# text='We use ptython ptython t acually t make a spell checker '   #input('Write text:')
# words=text.split()
# # print(words)
# with open('wordlist.txt') as f:
#     content=f.read()
#     words2=content.lower().split()
#     # print(words2)
#     for i,word in enumerate(words):
#         if word.lower() not in words2:
#             words[i]=f'*{word}*'
#     new_txt=' '.join(words)
# print(new_txt)




