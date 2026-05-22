 # operators
'''x=30
y=15
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)#remainder
print(x ** y) #x^Y'''

# relatonal operators(output is either true or false)
'''a=20
b=30
print(a > b)
print(a <= b)

sar=12
sar **= 3
print(sar)'''

# logical operators
'''a=1
b=2
print(a>b)
print(not a>b)

num1=True
num2=False
print(num1 or num2)
print('or operator:', num1 and num2)
print("or operator;", (a == b  or a > b)) '''

# Type conversion
'''a=int('65')
print(type(a))
b=float('87')
print(type(b))
print(a+b)
x=55
x=str(x)
print(type(x))'''

# input statements
'''length=int(input('lenght='))
breadth=int(input('breadth='))
area=length*breadth
print('area of square=',area) '''

''' x=float(input('number1='))
y=float(input('number2='))
average=(x+y)/2
print(average) '''

''' a=int(input('first:'))
b=int(input('second:'))
print(a>=b) '''

# LECTURE 2 STRINGS AND CONDITIONALS
# string operations
'''str1='sagar'  # concatenation(addition of string)
str2='bhattarai'
print(str1+str2)
print('sagar'+'bhattarai') '''
'''s1="ranxod das"  # len(string) = lenght of string
l1=len(s1)
s2="three idiots"
l2=len(s2)
final_str=s1+' '+ s2
final_len=len(final_str)
print(s1,l1)
print(l2,s2)
print(final_str)
print(final_len) '''
# Index Numbers(INDEXING)
'''s='sagar bhattarai'
print(s[3]+s[5] +s[2])
print(s[5])'''
# Slicing(important for machine learning)
# Note: str[1:]=str[1:len(str)]=str[1:last]
    #   str[:last]=str[zero:last]
    #   str[:]=str[zero:last]
'''str ='sagar bhattarai'
print(str[1:4])
print(str[:])'''
# NEGATIVE INDEXING(SLICING)
# Note:negative index is only used in slicing,not 
#      normally as an index no.
'''a='apple'
print(a[-4:-1])
print(a[:-1])
print(a[-6:])'''
# lets practice
'''name=input('enter your name:')
print('length of users first name=',len(name))
print(name.count('s'))'''
# s="i am a programmer"
# print(s.endswith('fucker'))
# s=s.capitalize()
'''print(s.capitalize())
print(s.replace('a','f'))
print(s.replace('am','fuck'))
print(s.replace('programmer','student and a coder'))
print(s.find('z'))
print(s.count('mm'))'''

# CONDITIONAL STATEMENTS[CORE CONCEPT]
'''age = 19
if age>=18:
    print('person can vote') # indentation
    print('person can also drive')
else:
    print('you are still immature') '''

'''light='green'
if(light=='red'):
    print('STOP')
elif(light=='green'):
    print('GO')
elif(light=='yellow'):
    print('LOOK AND GO')'''

'''marks=21
if(marks>=90):
    grade='a'
elif(80<=marks<90):
    grade='b'
elif(70<=marks<80):
    grade='c'
else:
    grade='d' 
print('grade of student:',grade)'''

# NESTING
'''age = 673
if(age>=18):
    if(age>=70):
        print('can not drive')
    else:
        print('can drive')

else:
    print('cannot drive')'''

#  LETS PRACTICE
"""num = 21
r=num%2 # remainder
if(r==0):
    print('number is even')
else:
    print('number is odd') """   

'''a=35
b=24
c=12
if(a>b and a>c):
    print('a is greatest number')
elif(b>a and b>c):
    print('b is the greatest number')
else:
    print('c is the greatest number ')'''

#  FORMATTING(F-STRING)
'''good = 'apple'
p = 200.679865
print(f'{good} price is {p:.3f}')
print(f'{{good}} price is {{p:.2f}}')'''

# STRING FUCTIONS
'''a = 'programmING is a good carrier '
print(a.upper(),a.lower())
print(a.rstrip('!'))
print(a.replace('m','#'))
print(a.capitalize())
print(a.center(30))
print(len(a))
print(len(a.center(30)))
print(a.endswith("G",)) # true
print(a.endswith("g",)) # false
print(a.title()) '''# capitalize first letter of each word in a sentence
'''s = "receipt"
print(s.center(20,'-'))
print(s.ljust(20,'-'))
print(s.rjust(20,'='))'''

# LIST
# Note:strings are unchangable in python
#      tuples are unchangable in python
#      lists are changable
'''marks = [24,12,74,27,94,23]
print(marks)
print(type(marks))
print(marks[3],marks[0])
print(marks[3]+marks[0])
print(len(marks))

student = ['sagar',54,'@@']# This is a list
student[0] = 'thaneshwor' # Now this works!        
print(student[0])
print(student)
print(marks[1:4])
print(marks[:-1])'''

# List Methods
'''l=[2,1,3,4]
l.append(5) # adds 5 in the end
l.sort() # ascending order
l.sort(reverse=True) # descending order
print(l)'''

'''l=['mango','apple','litchi','banana']
l.sort()
l.reverse()
l.insert(1,4)
l.remove('litchi')
l.pop(2)
print(l)'''

# Tuples 
# note: t=(1) type(t)=integer
#       t=(1,) type(t)=tuple [comma only in case of single member]
# slicing same as string and list
'''tup = (2,8,3,1,8)
print(tup.index(2)) # returns index of 2 first occurence
print(tup.count(8))''' # counts frequency of 8 = 2

# Dictionary 
# dictionary is changable,it don't have index/order
'''info={'age':20,
      'language':'python',
      12.6:834}
print(info)
print(info['age'])
print(info['language'])
print(12.6)
info['name']='sagar'
print(info)'''

# Nested Dictionary
'''student={
    'name':'sagar bhattarai',
    'age':20,
    'subject':{
        'physics':97,
        'math':86,
        'stat':73,
    }
}
print(student)
print(student['subject'])
print(student.keys()) # name,subject
print(len(tuple(student.keys())))
print(student.values())
print(student['age']) 
print(student.get('name')) 
student.update({'address':'Devdaha-04,Rupandehi'}) # address added
student.update({'name':'thaneshwor'}) # name updated
print(student)
new={'name':'tyson','age':21}
print(student)'''

# Set In Python
# have no order,each element must be unique and unchangable
# list and dictionary cannot be stored in set as they are changable
# note that set is changable,but set elements are unchangable
'''sett={1,2,3,4,4,5,'string'}
print(sett,type(sett))
sett2={} # this is dictionary
sett3=() # now this is empty set ;tuple
print(type(sett2),type(sett3))'''
'''collection=set()
collection.add('sagar')
collection.add(12)
collection.add((1,2,3)) # tuple can be stored in set
collection.add('thaneshor')
print(collection)
collection.remove('sagar')
print(collection)
collection.pop() # remove random value,can be any
print(collection)
collection.clear()
print(collection)'''

# Union and Intersection
'''set1={1,2,3,4,5,5,5}
set2={3,4,5,6}
print('Union:',set1.union(set2))
print('Union:',set2.union(set1)) # Same as Above
print('Intersection:',set1.intersection(set2))
print('Intersection:',set2.intersection(set1))
print(len(set1)) # 5 because 5,5,5 counts one
'''
# Lets Practice
# 1 : adding element on empty dictionary
'''marks={}
marks.update({'phy':21})
marks.update({'math':29})
marks.update({'stats':25})
print('marks:',marks)'''

# storing 9 and 9.0 as seperate values in set
# note that set identies 9 and 9.0 as same 

# loops
#  note: every loop must have a stopping point
# while loop
'''count=1
while count<=5:  # stopping condition
    print('hello')
    count+=1
print(count)

# i=1
# while i<=100:  # stopping condition
#     print('sagar',i)
#     i+=1
i=1
while i<=5:   # stopping condition
    print(i)
    i+=1
j=5
while j>=1:   # stopping condition
    print(j)
    j-=1'''

#  lets practice
# printing no from 1 to 100 and 100 to 1
'''a=1
while a<=100:  # stopping condition
    print('a=',a)
    a+=1
b=100
while b>=1:   # stopping condition
    print('b=',b)
    b-=1'''

#  table of a no
'''n=int(input('enter a number:'))
a=1
while a<=10:
    print(f'{n}*{a}=',(n*a)) 
    a+=1'''

# list of square of numbers from 1 to 10
'''n=1
while n<=10:
    print(f'{n}**2=',n**2)
    n+=1

num=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx <= (len(num)-1):
    print(num[idx])
    idx += 1'''

# searching a particular number in tuple
'''tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input('enter a number from tup :'))
i = 0
if x in tup:
    while i <= (len(tup)-1):
        if tup[i] == x:
            print(f"number {x} found at index {i}")
        i += 1  # This should be outside the if block
else:
    print('invalid number!')'''

# break and continue
'''i=0
while i<=5:
    if i==3:  # stops at i=2
        break
    print(i)
    i+=1'''

'''j=1
while j<=20:
    j+=1
    if j%2 == 0:
        continue
    print(j)'''

# for loops
# l=[1,2,3,7]   
# for el in l:
#     print(el)

'''tup=(8,6,4,2)
for num in tup :
    print(num)

s = 'programming  career'
for letters in s :
    print(letters)'''

# searching a particular number in tuple(using for loop)
'''tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x=49
idx=0
for el in tup:
    idx+=1
    if el==x:
        print(f'number found at index {idx}')'''
        # break

#  range
'''seq=range(5)  # range(5) == range(0,5)
print(range(5),seq)  # seq == range(5)
for i in seq:
    print(i)
print(seq[0],seq[1],seq[2],seq[3],seq[4])

for j in range(2,20,3): # range(start,stop,step difference)
    print(j)'''

#  lets practice
# print no from 1 to 100
'''for numbers in range(1,101):
    print(numbers)'''
# print no from 100 to 1
'''for num in range(100,0,-1):
    print(num)'''
# print multiplication table of a number
'''n=int(input('enter a number :'))
for m in range(1,11):
    print(f'{n}*{m}={n*m}')'''

# loops 2.o
'''name='thaneshwor' 
for i in name:
    print(i)
    if i==name[-1]:
        print('done')'''

'''for i in range(1,10):
    print(f'3*{i}=',(3*i))
    if i==5:
        break
print('loop ko xod ke nikal gaya')'''
 
'''for i in range(1,10):
    print(f'3*{i}=',(3*i))
    if i==5:
        print('skipped the iteration')
        continue'''
       
'''for i in range(1, 10):
    if i == 5:
        print('Skipped iteration 5')
        continue
    print(f'3 × {i} =', (3 * i))'''
     

# file input/output








       
    


        
   
   
        
        
    



    

    

    

 




  



 