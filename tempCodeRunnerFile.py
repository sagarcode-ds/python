#  i am learning Python
#  i will become a data scientist


# f=open('sample.txt','a+')   # a or w
#  r+ file gets trunket or rewrited
# even if sample.txt' doest not exists it gets created automatically
# l1=f.readline()
# print(l1)
# l2=f.readline()
# print(l2)
# f.close()
# f.write('\n #i am good \n #hahaha')  
# f.close()
# f.write('c')
# print(f.read())
# # print(f.read())
# f.close()

# with open('sample.txt','r') as f:
#     data=f.read()
#     print(data)
   

# with open('sample.txt','w') as f:
#     f.write('get up,code,eat,sleep,repeat')

# import os

# with open("sample.txt", "w") as f:
#     f.write("hello")

# os.remove("sample.txt")

# problems
# with open('practice.txt','w') as f:
#     f.write('Hi everyone\nwe are learning file i/o\n')
#     f.write('using java\ni like programming in java')

# with open('practice.txt','r') as f:
#     data=f.read()
#     # print(data,type(data))
# new=data.replace('java','python')
# print(new)

# with open('practice.txt','w') as f:
#     f.write(new)

# with open('practice.txt','r') as f:
#     data=f.read()
# print('learning' in data)

# def check_line():
#     line = 1
#     with open('practice.txt', 'r') as f:
#         while True:
#             data = f.readline()
#             if not data:  # End of file
#                 break
#             if 'using' in data:
#                 print(line)
#                 return
#             line += 1
#     print(-1)

# check_line()

# 🟢 Easy — Problem 1: Personal Journal Entry
# What to build: Write a program that:

# Asks the user to type a journal entry
# Saves it to journal.txt
# Reads it back and prints: "You wrote: [entry]"

# Hint: You'll need input(), open() with "w" mode, then open() with "r" mode.

# j=input('enter a journal entry:')
# with open('journal.txt','w') as f:
#     f.write(j)
# with open('journal.txt','r') as f:
#     content=f.read()
#     print('You wrote:',content)

# Problem 2: Line Counter
# What to build: Write a function count_lines(filename) that returns how many lines are in a file.
# Hint: readlines() returns a list. What property of a list tells you how many items are in it?

# created new file first
# with open('sample.txt','w') as f:
#     f.write('hello'+'\n')
#     f.write('sagar'+'\n')
#     f.write('how'+'\n')
#     f.write('are'+'\n')
#     f.write('you ?'+'\n')

# # now checking no of lines
# def count_lines(file):
#     line=0
#     with open(file,'r') as f:
#         for _ in f:
#             line+=1
#     return line
# print(count_lines('sample.txt'))


# Problem 3: Word Frequency Counter
# What to build: Given a text file, count how many times each word appears and print the top 5 most common words.
# Hint: Read the file, split into words (.split()), use a dictionary to count. Then sort the dictionary by value.

# with open('sample.txt','r') as f:
#     text=f.read().lower().strip().replace('.','')
#     # print(text)
#     words=text.split()
#     d={}
#     for word in words:
#         d[word]=d.get(word,0)+1
#     sorted_d=list(sorted(d.items(),key=lambda item: item[1],reverse=True))[:5]
#     for k,v in sorted_d:
#         print(f"{k} : {v}")


#  read line by line
# with open('sample.txt','r') as f:
#     i=1
#     for line in f:
#         print(f'line {i} : {line.strip()}')
#         i+=1

# count characters total

# with open('sample.txt','r') as f:
#     content=f.read().strip()
#     print(len(content))

# count total words in file

# with open('sample.txt','r') as f:
#     content=f.read()
#     words=content.split()
#     # print(words)
#     print(len(words))
#     # unique words only
#     print(len(set(words)))

# count lines in file
# with open('sample.txt','r') as f:
#     # content=f.read()
#     c=0
#     for line in f.strip():
#         c+=1
#     print(c)

# # find specific word in file
# w=input('enter word :')
# found=False
# with open('sample.txt','r') as f:
#     content=f.read()
#     words=content.split()
#     # print(words)
#     for word in words:
#         if w.lower()==word.lower():
#             found=True
#             break
#     if found:
#         print('found')
#     else:
#         print('not found')


# # count specific word frequency
# with open('sample.txt','r') as f:
#     content=f.read().lower()
#     d={}
#     for p in ".,!?;:'\"()[]{}":
#         content = content.replace(p, '')
#     words=content.split()
#     for word in words:
#         d[word]=d.get(word,0)+1
#     # print(d)
#     for k,v in d.items():
#         print(f'{k} appears {v} times')

# copy file content to another file
# with open('sample.txt','r') as f1,open('newfile.txt','w') as f2:
#     for line in f1:
#         f2.write(line)
    
# # mini project

# with open('sample.txt','r') as f:
#     l=0
#     content=f.read().lower()
#     f.seek(0)
#     for line in f:
#         l+=1
#     # print(l)
#     for p in ".,!?;:'\"()[]{}":
#         content = content.replace(p, '')
#     words=content.split()
#     d={}
#     for word in words:
#         d[word]=d.get(word,0)+1
#     sorted_d=list(sorted(d.items(),key=lambda item: item[1],reverse=True))[:5]
#     w=input('enter a word:')


#     print('--- FILE ANALYSIS REPORT ---')
#     print('total lines:',l)
#     print('total words:',len(words))
#     print('unique words:',len(set(words)))
#     print()
#     print('top 5 most common words:')
#     for k,v in sorted_d:
#         print(f'{k} : {v}')
#     print('search result:')
#     if w in d:
#         print(f'{w} found {d.get(w)} times')
#     else:
#         print(f'{w} not found')

# #  print lines of file in reverse order
# with open('sample.txt','r') as f:
#     lines=f.readlines()
#     for l in reversed(lines):
#         print(l.strip())

# # create a new file by removing empty lines from a file
# with open('sample.txt','r') as f1,open('newfile.txt','w') as f2:
#     for line in f1:
#         if line.strip():
#             f2.write(line)
        
# Problem M2: File Merger
# Write a program that:

# Takes two filenames as input (e.g., file1.txt, file2.txt)
# Combines their content into a new file called merged.txt
# Adds a separator line --- FILE BREAK --- between them

# file1=input('enter filename:')
# file2=input('enter filename:')
# with open(file1,'r') as f1,open(file2,'r') as f2:
#     with open('merge.txt','w') as f3:
#         f3.write(f1.read())
#         f3.write('\n--- FILE BREAK ---\n')
#         f3.write(f2.read())


# Write a program that:

# Reads a file grades.txt where each line is: StudentName Score (e.g., Alice 85)
# Calculates the average score
# Finds the highest and lowest scoring students
# Writes a summary report to report.txt

with open('grade.txt','r') as f:
    d={}
    for line in f:
        d[line.split()[0]]=int(line.split()[1])
    # print(list(d.items()))
    score=list(d.items())
    highest_mark=score[0][1]
    highest_std=score[0][0]
    for item in score[1:]:
        if item[1]>highest_mark:
            highest_mark=item[1]
            highest_std=item[0]
    lowest_mark=score[0][1]
    lowest_std=score[0][0]
    for item in score:
        if item[1]<lowest_mark:
            lowest_mark=item[1]
            lowest_std=item[0]
    summ=0
    for i in score:
        summ+=i[1]
    average=summ/len(score)
with open('report.txt','w') as f2:
    f2.write('--summary report--')
    f2.write(f'\ntotal students:{len(d)}')
    f2.write(f'\naverage score :{average}')
    f2.write(f'\nhighest score achieved by {highest_std}, score:{highest_mark}')
    f2.write(f'\nlowest score achieved by {lowest_std}, score:{lowest_mark}')


# 🏋️ Final Exercise
# Put everything together. Write a program that:

# Creates a file students.txt with at least 5 student names (one per line)
# Reads the file back and prints all names in uppercase
# Appends a new student name to the file
# Counts how many students are in the file total

with open('students.txt','w') as f:
    f.write('sagar')
    f.write('\nbob')
    f.write('\nalice')
    f.write('\ntyson')
    f.write('\npriya')
    f.write('\nriya')
with open('students.txt','r') as f2:    
    lines=f2.readlines()
    for std in lines:
        print(std.strip().upper())
with open('students.txt','a+') as f3:
    f3.write('\nmicheal')
    f3.write('\ntom')
    f3.seek(0)
    print('total students:',len(f3.readlines()))
 

        
    

