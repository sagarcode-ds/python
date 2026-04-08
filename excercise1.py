# VARIABLES AND IDENTIFIERS
'''name = 'sagar bhattarai'
age = 20
height = 1.02 
student = True
print(type(height))
print(type(height))
print(type(student))
print(type( age))'''

#  VALID VS INVALID IDENTIFIERS
# my_var=34
# 2nd_var (incorrect)
# _private='motorcycle'
# my-variable='her' NOTE: - is invalid (special character)
'''varaible_name='kohjh'
Class= 'bachelor'
print(Class) ''' # .class cannot be identifier because . is a special character 

# DATA TYPES IDENTIFICATION
'''var5 = 5+3j
var6 = [1,2,3]
var7 = (1,2,3)
var8 = {1,2,3}
var9 = {"name": "john", }
print(type(var5))
print(type(var6))
print(type(var7))
print(type(var8))
print(type(var9))'''

# MEMORY ADDRESSES
'''a=5
b=5
print(id(a))
print(id(b)) # a=b then a and b have same memory address
x=a
print(id(x)) '''

# PRINT STATEMENT
# print('apple','banana',sep='@')
# print(25,12,end='')
"addition"
"sagar"
'''name='sagar'
age=20
score=3.75
print(name,age,score)
print('name:',name, 'age:',age)
print("name"+name+'age;'+age)'''
# some excercises are pending for later

# OPERATORS
"""a=10
b=3
addition=a+b
sub=a-b
mult=a*b
div=a/b
print(addition,sub,mult,div)
print(a%b) # % = remainder
print(a**b)
print('floor division:',a//b)"""  #floor division
# Comparison operators
'''print(10>5)
print(10==10.0)
print("hello" == "Hello")
print(7 <= 7)
print(15>=20) '''
# Logical operators
'''x=True
y=False
z=True
print(x and y)
print(x or y)
print(not y)
print(x and (y or z))
print(not(x and y)) '''
# Assignment operators
'''num=10
num -= 5 # it means num = num + 5
print(num)
num *= 2
print(num)
num %= 14 # only shows remainder not quotent
print(num)
num **= 2
print(num) '''
# excercise 4.5 is pending to solve

# TYPE CASTING
# explicit
'''a=int(15.8)
print(a)
b=42
b=float(b)
print(type(b))
c=str(100)
print(type(c))
d=float("3.14")
print(d)
j=bool(0)
print(type(j))
l=bool("hello")
print(type(l)) '''
# implicit
"""print(type(False + 10)) #   TYPE IS STILL AN INTEGER
print(type(True))"""

# EXERCISE 6 : COMBINED PROBLEM
# Temperature converter
'''c=35
f=(c*9/5)+32
print('temperature in celcius:',c,)
print('temperature in fahrenheit:',f) '''
# simple calculator is yet to be solved

# user information display
'''name='sagar'
age=20
city='butwal'
profession='student'
current_year=2026
birth_year = current_year-age 
print("user information")
print('name:',name)
print('age:',age)
print('city:',city)
print('professtion:',profession)
print("Birth year:",birth_year)
print('good morning',name) '''

# shopping cart
'''apple=150
banana=120
orange=100
Total_cost = apple+banana+orange
print("===Itemized Bill===")
print('apple price:',apple)
print('banana price:',banana)
print('orange price:',orange)
print('Total cost:',Total_cost)
discount = 10/100 * Total_cost
print('Discount:',discount)
final_amount= Total_cost-discount
print('Final amount:',final_amount) '''

# # challenge 1 : swap variables  '''a=5
# b=10
# a,b = b,a
# print(a)
# print(b) '''

# challenge 2 : type detective
# pending for splving

# challenge 3 : operator precedence
'''result1 = 10+3*2
print(result1)
result5 = 10>5 and 3<4 or True 
print(result5) '''
'''
a = 5
b = 10
sum = a+b
diff = a-b
product = a*b
quotient = a/b
print("sum=",sum, 'diff=',diff, 'product=',product, 'quotient=',quotient)
'''

# simple calculator
''' n=float(input('first num:'))
m=float(input('second num:'))
print('sum=',n+m)
print('diff=',n-m)
print('product=',n*m)
print('quotient=',n/m) '''

# input fucnction excercises deepseek
'''a = float(input('enter first number:'))
b = float(input('enter second number:'))
print('sum=',a+b)
print('diff=',a-b)
print('product=',a*b)
print('quotient=',a/b) '''

'''l=float(input("enter length:"))
b=float(input("enter breadth:"))
print("area=",l*b)
print("perimeter=",2*(l+b)) '''

'''name=input("enter student name:")
m1=int(input("enter math mark:"))
m2=int(input("enter science mark:"))
m3=int(input("enter english mark:"))
print('Total mark=',m1+m2+m3)
print('average mark=',(m1+m2+m3)/2) '''

''''T=float(input('temperature in celsius:'))
F=(T*9/5)+32
print('celsious:',T)
print('fahrenheit:',F) '''

'''p=float(input('principal='))
r=float(input('rate of interest='))
t=float(input('time(in year)='))
print('principal:',p)
print('rate of interest:',r)
print('time:',t)
print("simple interest:",(p*t*r)/100)
print('total amount:',p+((p*t*r)/100)) '''

'''a=int(input('1st num='))
b=int(input("2nd num="))
c=int(input('3rd num='))
print('Steps to calculate (a+b)*c/2')
print('step 1:a+b=',a+b)
print('step 2:c/2=',c/2)
print('step 3:(a+b)*c/2=',(a+b)*c/2) '''

'''s=int(input('enter time in seconds:'))
m=s/60
print('600 seconds=',m,'minute') '''

'''f=input('enter first name:')
l=input('enter last name:')
print('full name:',f,l)
print('length of full name=12')'''

'''n=input('enter a number:')
i=int(n)
f=float(n)
print('string:',n)
print('integer:',i)
print('float:',f)'''
"""n=float(input('enter a number:'))
s=n**2
c=n**3
sr=n**0.5
print("square root=",round(sr,25))"""
# challenge 1 : shopping bill calculator
'''n=input('enter item name:')
p=float(input('enter price per unit of item:'))
q=float(input('enter quantity:'))
t=p*q
d=float(input('enter discount percent:'))
dp=t-(d/100*t)
print('---itemized bill---')
print('item name:',n)
print('price per unit:',p)
print('no of unit:',q)
print('total price:',t)
print('discout percent:',d)
print('Final price:',dp) '''

