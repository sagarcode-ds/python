# 1 : Student Grade Analyser
'''Write a program that:
1. Asks for the student's name and roll number (store as a tuple).
2. Asks how many subjects they have, then inputs marks for each subject (store marks in a list).
3. Calculates:
  · Total marks
  · Average percentage
 · Highest and lowest marks
4. Assigns a grade based on average:
   · ≥90 → A
   · 80–89 → B
   · 70–79 → C
   · 60–69 → D
   · <60 → F
5. Prints a report card showing: name, roll, marks list, total, average, grade, and whether they passed all subjects (each ≥40).
'''
'''
name = input('enter student name:')
roll = int(input('enter student roll no:'))
student_record=(name,roll)
subnum=int(input('How Many Subjects do you have? \n Ans:'))
mark1=int(input('enter mark in sub1:'))
mark2=int(input('enter mark in sub2:'))
mark3=int(input('enter mark in sub3:'))
mark4=int(input('enter mark in sub4:'))
marks=[mark1,mark2,mark3,mark4]
total_marks=sum(marks)
full_mark=100*subnum
a=(total_marks/full_mark)*100# average percentage
highest = max(marks)
lowest = min(marks)

if(a>=90):
    grade='A'
elif(a>=80):
    grade='B'
elif(a>=70):
    grade='C'
elif(a>=60):
    grade='D'
else:
    grade='F'

print('Report Card'.center(25))
print('-'*25)
print('Name:',student_record[0])
print('Roll NO:',student_record[1])
print('Marks:',marks)
print('Total Marks:',total_marks)
print('Average percentage:',a)
print('Grade:',grade)
if(lowest>=40):
    print('Student passed all the subject')
else:
    print('Student did not pass all the subject')
'''
# 2 : List Sorter And Analyser
'''Write a program that:
1. Asks the user to enter 5 numbers (store them in a list).
2. Prints the original list.
3. Asks the user what they want to do:
   · Type 'asc' to sort in ascending order.
   · Type 'desc' to sort in descending order.
   · Type 'rev' to reverse the list.
4. After performing the operation, print the modified list.
5. Also print the first and last element of the final list.'''

'''num1=int(input('enter 1st number:'))
num2=int(input('enter 2nd number:'))
num3=int(input('enter 3rd number:'))
num4=int(input('enter 4th number:'))
num5=int(input('enter 5th number:'))
num=[num1,num2,num3,num4,num5]
print('numbers',num)
choice=input('what you want to do?(asc/desc/rev) \n Ans:').lower()
if(choice=='asc'):
    num.sort()
    print('ascending order:',num)
elif(choice=='desc'):
    num.sort(reverse=True)
    print('descending order:',num)
elif(choice=='rev'):
    num.reverse()
    print('reverse order:',num)
else:
    print('invalid choice,please choose the valid input')

print('modified list:',num)
print('1st element of final list:',num[0])
print('last element of final list:',num[-1])'''

# Project 3: 2D Point Distance Calculator
'''Topics: Tuples, list of tuples, indexing, math.sqrt, conditionals, formatting

Write a program that:

1. Asks the user for the x and y coordinates of 3 points.
2. Stores each point as a tuple (x, y) inside a list called points.
3. For each point, calculate its distance from the origin (0,0) using the formula:
      distance = sqrt(x² + y²)
      You need to import math and use math.sqrt().
4. Print each point and its distance.
5. Find which point is closest to the origin (use min() with a key or compare manually with if).
6. Print the closest point.'''

'''x1=int(input('enter x coordinate of point1:'))
y1=int(input('enter y coordinate of point1:'))
x2=int(input('enter x coordinate of point2:'))
y2=int(input('enter y coordinate of point2:'))
x3=int(input('enter x coordinate of point3:'))
y3=int(input('enter y coordinate of point3:'))
point1=(x1,y1)
point2=(x2,y2)
point3=(x3,y3)
points=[point1,point2,point3]
distance1=(x1**2+y1**2)**0.5
distance2=(x2**2+y2**2)**0.5
distance3=(x3**2+y3**2)**0.5
d=[distance1,distance2,distance3]
print('Point 1 :',point1)
print('Distance of point1 from origin :',round(distance1,2))
print('Point 2 :',point2)
print('Distance of point2 from origin :',round(distance2,2))
print('Point 3 :',point3)
print('Distance of point3 from origin :',round(distance3,2))
if(min(d)==distance1):
    closest=point1
elif(min(d)==distance2):
    closest=point2
elif(min(d)==distance3):
    closest=point3
print('Closest point from origin :',closest)'''

# Project 4: Fixed‑Size Shopping Cart
'''Topics: List of tuples, indexing, arithmetic, string formatting, .pop() method
Write a program that:
1. Asks for 3 items. For each item, ask for:
   · Name
   · Price
   · Quantity
     Store each item as a tuple (name, price, qty) inside a list called cart.
2. Calculate the total cost:
      total = cart[0][1]*cart[0][2] + cart[1][1]*cart[1][2] + cart[2][1]*cart[2][2]
3. Print a receipt with right‑aligned columns (use .rjust() or f‑string formatting).
4. Ask the user: “Which item index (0,1,2) do you want to remove?”
5. Remove that item using cart.pop(index).
6. Recalculate the total without that item and print the updated receipt.'''

# Project 5: Five‑Number Statistics
'''Write a program that:
1. Asks the user to enter 5 numbers (store in a list).
2. Calculates and displays:
   · The list itself
   · Count (use len)
   · Sum (sum)
   · Average (sum / len)
   · Maximum (max)
   · Minimum (min)
3. Sort the list (using sorted() which returns a new list) and find the median:
   · Since there are 5 numbers, the median is the middle element after sorting: sorted_numbers[2].
4. Optional (if you want a challenge): Find the mode (most frequent number). Because the list is small, you can check frequencies manually using if statements (e.g., compare each number with others). If multiple numbers appear equally often, you can pick any.'''
'''
num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
num3=int(input('enter third number:'))
num4=int(input('enter fourth number:'))
num5=int(input('enter fifth number:'))
num=[num1,num2,num3,num4,num5]
print('count=',len(num))
print('Sum=',sum(num))
print('average=',sum(num)/len(num))
print('maximum=',max(num))
print('minimum=',min(num))
num.sort()
print('median=',num[2])'''

# Project 6: Classroom Roll Call (List of Names)

'''Topics: List, indexing, .append(), .pop(), .index(), .count(), conditionals

Create a program that manages a list of 5 student names.

1. Start with an empty list and ask the user to enter 5 names (append each).
2. Display the list with their indices (0 to 4).
3. Ask the user for a name to search for:
   · If found, print its index (use .index(name)).
   · If not found, print "Not in list".
4. Ask the user for an index to remove (0–4). Remove that name using .pop(index) and print the updated list.
5. Count how many names start with a vowel (a, e, i, o, u) – you'll need to check each name manually (since no loops, use separate if for each index).'''

'''name=[]
name.append('sagar')
name.append('thaneshwor')
name.append('riya')
name.append('tyson')
name.append('priya')
print('name:',name)
index=(name.index('sagar'),name.index('thaneshwor'),name.index('riya'),name.index('tyson'),name.index('priya'))
print('indices:',index)
search=name.index('m')
print(search)'''

# Project 7: Temperature Converter (Celsius to Fahrenheit) SCORE 9/10
'''Topics: List, arithmetic, tuple for conversion factors, string formatting
Write a program that:
1. Asks for 5 temperatures in Celsius, stores them in a list.
2. Creates a tuple FACTORS = (9/5, 32) for conversion formula:
      Fahrenheit = Celsius * FACTORS[0] + FACTORS[1]
3. Converts each Celsius temperature to Fahrenheit without loops – use separate variables for each converted value (e.g., f0 = c0 * FACTORS[0] + FACTORS[1], etc.)
4. Prints a table showing Celsius and Fahrenheit side by side, aligned nicely.
5. Also prints the average Celsius and average Fahrenheit.'''
'''c0=float(input('enter temp1:'))
c1=float(input('enter temp2:'))
c2=float(input('enter temp3:'))
c3=float(input('enter temp4:'))
c4=float(input('enter temp5:'))
print('-'*25)
c=[c0,c1,c2,c3,c4]
factors=(9/5,32)
f0=c0*factors[0]+factors[1]
f1=c1*factors[0]+factors[1]
f2=c2*factors[0]+factors[1]
f3=c3*factors[0]+factors[1]
f4=c4*factors[0]+factors[1]
print('Table'.center(25))
print('-'*25)
print('-'*25)
print('celcius'.ljust(12)+'fahrenheit'.rjust(13))
print(f'{c0:<12}{f0:>13}')
print(f'{c1:<12}{f1:>13}')
print(f'{c2:<12}{f2:>13}')
print(f'{c3:<12}{f3:>13}')
print(f'{c4:<12}{f4:>13}')
print('-'*25)
print('Average celcius temperature=',(c0+c1+c2+c3+c4)/len(c))
print('average fahrenheit temperature=',(f0+f1+f2+f3+f4)/len(c))'''

# Project 8: Word Analyzer (Fixed 5 Words) SCORE 7.5/10
# Note:if = check this condition independently  
#elif = only check if ALL previous conditions were FALSE
'''Topics: List, string methods, indexing, conditionals
Write a program that:
1. Asks the user to enter 5 words, stores them in a list.
2. Finds and prints:
   · The longest word (if tie, pick the first)
   · The shortest word
   · Total characters (sum of lengths)
   · Number of words that contain the letter 'e' (case‑insensitive)
3. Asks the user for a letter, then checks each word (manually) whether it starts with that letter, and prints those words.'''
'''word1='sagare'
word2='bhattarai'
word3='thaneshowr'
word4='micheal'
word5='tyson'
words = [word1, word2, word3, word4, word5]
# Code correction part
# CORRECT approach - compare with the CURRENT longest/shortest
longest = word1
if len(word2) > len(longest):  # Compare with longest, not word1
    longest = word2
if len(word3) > len(longest):  # Compare with longest, not word1
    longest = word3
if len(word4) > len(longest):  # Compare with longest, not word1
    longest = word4
if len(word5) > len(longest):  # Compare with longest, not word1
    longest = word5
print('Longest word :',longest)
print('Lenghth of longest word:',len(longest))
shortest=word1                   # Note:if = check this condition independently  
if(len(word2)<len(shortest)):      #      elif = only check if ALL previous conditions were FALSE
    shortest=word2
if(len(word3)<len(shortest)):
    shortest=word3
if(len(word4)<len(shortest)):
    shortest=word4
if(len(word5)<len(shortest)):
    shortest=word5
print('shortest word:',shortest)
print('length of shortest word:',len(shortest))
print('Total Characters:',len(word1)+len(word2)+len(word3)+len(word4)+len(word5))
ecount=0
if('e' in word1.lower()):
    ecount=ecount+1
if('e' in word2.lower()):
    ecount=ecount+1
if('e' in word3.lower()):
    ecount=ecount+1
if('e' in word4.lower()):
    ecount=ecount+1
if('e' in word5.lower()):
    ecount=ecount+1
print('No of words containing e :',ecount)
letter = input('Enter a Letter :')
if(words[0][0].lower()==letter):
    print(f"{words[0]} starts with {letter}")
if(words[1][0].lower()==letter):   
    print(f"{words[1]} starts with {letter}") 
if(words[2][0].lower()==letter): 
    print(f"{words[2]} starts with {letter}")
if(words[3][0].lower()==letter):
    print(f"{words[3]} starts with {letter}")
if(words[4][0].lower()==letter):
    print(f"{words[4]} starts with {letter}")
else:
    print(f"no word starts with {letter}")'''


# Project 9: Movie Ratings Analysis (Two Parallel Lists)  SCORE 9.5/10
'''Topics: List, tuple, indexing, arithmetic, conditionals
Create two lists: one for movie titles, one for ratings (out of 5). They must be parallel (same index corresponds to same movie).
1. Ask the user for 4 movies. For each, get title and rating, and append to respective lists.
2. Print both lists side by side.
3. Find and print:
   · The highest‑rated movie (if tie, print the first)
   · The lowest‑rated movie
   · Average rating
4. Ask the user for a threshold rating (e.g., 4). Print all movies with rating ≥ threshold (manually check each index).'''
'''movie1=input('enter first movie name :')
r1=float(input('enter first movie rating:'))
movie2=input('enter second movie name :')
r2=float(input('enter second movie rating:'))
movie3=input('enter third movie name :')
r3=float(input('enter third movie rating:'))
movie4=input('enter fourth movie name :')
r4=float(input('enter fourth movie rating:'))
titles=[movie1,movie2,movie3,movie4]
ratings=[r1,r2,r3,r4]
print(f"{movie1}({r1})")
print(f"{movie2}({r2})")
print(f"{movie3}({r3})")
print(f"{movie4}({r4})")
highest_rated=ratings[0]
highest_movie=titles[0]
if(ratings[1]>highest_rated):
    highest_rated=ratings[1]
    highest_movie=titles[1]
if(ratings[2]>highest_rated):
    highest_rated=ratings[2]
    highest_movie=titles[2]
if(ratings[3]>highest_rated):
    highest_rated=ratings[3]
    highest_movie=titles[3]
print('Highest rated movie :',highest_movie)
print('Rating :',highest_rated)
lowest_rated=ratings[0]
lowest_movie=titles[0]
if(ratings[1]<lowest_rated):
    lowest_rated=ratings[1]
    lowest_movie=titles[1]
if(ratings[2]<lowest_rated):
    lowest_rated=ratings[2]
    lowest_movie=titles[2]
if(ratings[3]<lowest_rated):
    lowest_rated=ratings[3]
    lowest_movie=titles[3]
print('Lowest rated movie :',lowest_movie)
print('Rating :',lowest_rated)
print('Average Rating :',(r1+r2+r3+r4)/len(ratings))
threshold=float(input("Enter threshold rating:"))
if(ratings[0]>=threshold):
    print(f"{titles[0]}-rating:{ratings[0]}")
if(ratings[1]>=threshold):
    print(f"{titles[1]}-rating:{ratings[1]}")
if(ratings[2]>=threshold):
    print(f"{titles[2]}-rating:{ratings[2]}")
if(ratings[3]>=threshold):
    print(f"{titles[3]}-rating:{ratings[3]}")'''

# Project 10: To‑Do List with Priorities (List of Tuples) Score 10/10
'''Topics: List of tuples, indexing, .pop(), tuple unpacking, sorting
Build a simple to‑do list where each task is a tuple: (priority, description) with priority 1 (high) to 3 (low).
1. Start with an empty list. Ask for 3 tasks (priority and description), append as tuples.
2. Show the list (unsorted).
3. Ask the user: "Sort by priority? (yes/no)". If yes, sort the list using .sort() (which sorts by first element then second).
4. Show the sorted list.
5. Ask the user which task to mark as done (by index, 0‑2). Remove it with .pop(index) and print the updated list.
6. Print the highest priority task (lowest number) in the remaining list – you can find it by comparing manually (since only up to 3 tasks left).'''
'''tasks=[]
t1=input('enter task1:')
p1=int(input('enter task1 priority:'))
t2=input('enter task2:')
p2=int(input('enter task2 priority:'))
t3=input('enter task3:')
p3=int(input('enter task3 priority:'))
tasks.append((p1,t1))
tasks.append((p2,t2))
tasks.append((p3,t3))
print('tasks:',tasks)
sort=input('sort by priority? \n Ans:').lower()
if(sort=='yes'):
    tasks.sort()
print('Sorted Tasks :',tasks)
done1=int(input('which index task is done? \n Ans1:'))
if(0<=done1<len(tasks)):# corrected part
    tasks.pop(done1)  # done1<len(tasks), index(3) doesnot exists
    print('Updated List:',tasks)
else:
    print('invalid index.item with this index doesnot exist.')
if(len(tasks)>=2):  # corrected part
    if(tasks[0][0]<tasks[1][0]):
       print('highest prority task=',tasks[0])
    else:
        print('highest prority task=',tasks[1])
elif(len(tasks)==1):
    print('highest prority task=',tasks[0])
else:
    print('No task remaining')'''


    

