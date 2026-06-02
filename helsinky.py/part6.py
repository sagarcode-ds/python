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

# This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.
# Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.
# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter

# Meatballs
# 45
# mince
# eggs
# breadcrumbs

# Tofu rolls
# 30
# tofu
# rice
# water
# carrot
# cucumber
# avocado
# wasabi

# Cake pops
# 60
# milk
# bicarbonate
# eggs
# salt
# sugar
# cardamom
# butter
# Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then easier to manipulate in the way described in the exercise.
# Search for recipes based on the name of the recipe
# Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.
# An example of the function in action:
# found_recipes = search_by_name("recipes1.txt", "cake")
# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes
# Cake pops
# As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.
# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
# Search for recipes based on the preparation time
# Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.
# The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.
# found_recipes = search_by_time("recipes1.txt", 20)
# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes, preparation time 15 min
# Search for recipes based on the ingredients
# A word of caution: this third part of the exercise is considerably more demanding than the previous two. If you feel like you aren't making headway, it may be worth your while to move on, complete the other exercises in this part of the material, and then come back to this exercise if you have time later. Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.
# Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.
# The names of these recipes are returned in a list just like in the second part, with the preparation time appended. Please have a look at the example below.
# found_recipes = search_by_ingredient("recipes1.txt", "eggs")
# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min

# def read_recipe(filename):
#     with open(filename) as f:
#         foods=f.readlines()
#     foods.append('\n')
#     recipe=[]
#     name=''
#     time=''
#     ingrd=[]
#     for line in foods:
#         line=line.strip()
#         if line=='':
#             if name!='':
#                 d={'name':name,'prep time':int(time),'ingredients':ingrd}
#                 recipe.append(d)
#             name=''
#             time=''
#             ingrd=[]
#         elif name=='':
#             name=line
#         elif time=='':
#             time=line
#         else:
#             ingrd.append(line)
#     return recipe


# def search_by_name(filename,name):
#     recipes=read_recipe('foods.txt')
#     l=[]
#     for i in recipes:
#         if name.lower() in i['name'].lower():
#             l.append(i['name'])
#     return l
# print(search_by_name('foods.txt','cake')  )         

# def search_by_time(filename,time):
#     recipes=read_recipe('foods.txt')
#     l=[]
#     for i in recipes:
#         if time <= i['prep time']:
#             l.append(i['prep time'])
#     return l 
# print( search_by_time('foods.txt',15))
    
# def search_by_ingredients(filename,ingredient):
#     recipes=read_recipe('foods.txt')
#     l=[]
#     for i in recipes:
#         if ingredient in i['ingredients']:
#           l.append(i['name'])
#     return l

# print(search_by_ingredients('foods.txt','sugar'))

# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.
# Each file will follow this format:
# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.

# Distance between stations
# First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:

# Sample output
# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }
# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.
# Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.
# The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.
# # we will need the function sqrt from the math module 
# import math
# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)
# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)
# Sample output
# 0.9032737292463177
# 0.7753594392019532

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

# The greatest distance
# Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
# Sample output
# Laivasillankatu Hietalahdentori 1.478708873076181

# import math
# def get_station_data(filename):
#     with open(filename) as f:
#         d={}
#         for line in f:
#             parts=line.strip().split(';')
#             # print(parts)
#             if parts[0]=='Longitude':
#                 continue
#             d[parts[3]]=(float(parts[0]),float(parts[1]))
#     return d
# # print(get_station_data('stations.txt'))
# stations=get_station_data('stations.txt')
# # 1 distance between stations
# def distance(stations: dict, station1: str, station2: str):
#     x=(stations[station1][0]-stations[station2][0])*55.26
#     y=(stations[station1][1]-stations[station2][1])*111.2
#     distance_km = math.sqrt(x**2 + y**2)
#     return distance_km

# # 2 greatest distance
# def greatest_distance(stations):
#     max_distance=0
#     station1=''
#     station2=''
#     for st in stations:
#         for st2 in stations:
#             if st==st2:
#                 continue
#             d=distance(stations,st,st2)
#             if d>max_distance:
#                 max_distance=d
#                 station1=st
#                 station2=st2
#     return station1,station2,max_distance
# print(greatest_distance(stations))

# writing files

# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.
# The program should work as follows:
# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# When the program is executed for the second time, this should happen:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!
# def read_file(filename):
#     try:
#         with open(filename) as f:
#             content=f.read()
#         if content=='':
#             print('no entries available')
#         else:
#             print(content.strip())
#     except FileNotFoundError:
#             print('File does not exist')

            
            

# def write_file(filename):
#     text=input('Diary entry:')
#     with open(filename,'a') as f:
#         f.write(text+'\n')
#         print('Diary saved')
    
# read_file('diary.txt')
# while True:
#     print('1 - add an entry, 2 - read entries, 0 - quit')
#     c=input('function:')
#     if c=='0':
#         print('Bye now!')
#         break
#     elif c=='1':
#         write_file('diary.txt')
#     elif c=='2':
#         print('Entries:')
#         read_file('diary.txt')
    
# The file solutions.csv contains some solutions to mathematics problems:
# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.
# Please write a function named filter_solutions() which
# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.
# Please write the lines in the same order as they appear in the original file. Do not change the original file.
# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once
# filter_solutions()
# or multiple times in a row
# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()
# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.   

# def filter_solutions():
#     correct=[]
#     incorrect=[]
#     with open('solutions.csv') as f:
#         for line in f:
#             parts=line.strip().split(';')
#             if '+' in parts[1]:
#                 a,b=parts[1].split('+')
#                 if int(a)+int(b)==int(parts[2]):
#                     correct.append(line.strip())
#                 else:
#                     incorrect.append(line.strip())
#             elif '-' in parts[1]:
#                 x,y=parts[1].split('-')
#                 if int(x)-int(y)==int(parts[2]):
#                         correct.append(line.strip())
#                 else:
#                     incorrect.append(line.strip())
#             else:
#                 incorrect.append(line.strip())
                          
#     with open('correct.csv','w') as f:
#         for line in correct:
#             f.write(line+'\n')
#     with open('incorrect.csv','w') as f:
#         for line in incorrect:
#             f.write(line+'\n') 

# filter_solutions()
# filter_solutions()             
# filter_solutions()

# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.
# The tuple contains the following elements:
# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format
# name;age;height
# Each entry should be on a separate line. If we call the function with the argument ("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:
# Paul Paulson;37;175.5

# def store_personal_data(person: tuple):
#     line=''
#     for i in person:
#         line+=f'{i};'
#     line=line[:-1]
#     with open('people.csv','a') as f:
#         f.write(line+'\n')
# store_personal_data(('sagar',12,144))
# store_personal_data(('bob',12,5.6))

