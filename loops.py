# Project 2: Shopping List Manager
'''
Topics: Lists (of tuples), input, loops, conditionals, string methods
Create a program that manages a shopping list. Each item has a name, price, and quantity (store as a tuple inside a list).
Features:
1. Show a menu:
   · Add item
   · View list
   · Calculate total cost
   · Find most expensive item
   · Exit
2. When adding, ask for name, price, quantity, and append (name, price, qty) to the list.
3. View list – print each item neatly aligned.
4. Total cost = sum of price × quantity.
5. Most expensive item – compare prices (if tie, pick first).
'''

'''menu=[]
# asssume the follwing hard coded name,price,quantity as input
name1='apple'
price1=200
quantity1=63
name2='mango'
price2=250
quantity2=72
name3='orange'
price3=300
quantity3=45
item1=(name1,price1,quantity1)
item2=(name2,price2,quantity2)
item3=(name3,price3,quantity3)
menu.append(item1)
menu.append(item2)
menu.append(item3)
print('menu :',menu)
total = 0
for item in menu:
    total = total + (item[1] * item[2])
print("Total cost:", total)
most_expensive=menu[0][0]
max_price=menu[0][1]
if menu[1][1]>max_price:
    max_price=menu[1][1]
    most_expensive=menu[1][0]
if menu[2][1]>max_price:
    max_price=menu[2][1]
    most_expensive=menu[2][0]
print(f"most expensive item : {most_expensive} with price : {max_price}")
print('code exited')'''



#  finding sum from 1 to N
'''sum=0
for i in range(1,21):
    sum+=i
print(sum)'''

# how many no are divisible by 3(1-50)
'''c=0
for i in range(1,51):
    if i%3==0:
        c+=1
print(c)'''

# count no of vowels in string
'''strr='i am a data scientist'
c=0
for l in strr:
    if l.lower() in 'aeiou':
        c+=1
print(c)'''

# finding largest element in the list
'''l=[1,2,3,4,5]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print(largest)'''
    
# finding smallest element in the list
'''l=[1,2,3,4,5]
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print(smallest)'''

# counting how many times a no appears in list
'''l=[1,2,2,2,3,4,8,8,8,8]
n=int(input('enter no to count its occurence:'))
if n in l:
    c=0   
    for i in l:
        if i==n:
            c+=1
    print(c)
else:
    print(f'no {n} is not inside list')'''

# finding longest word in a sentence
'''s='i will be a data scientist within a year'
words=s.split()
longest= ''
for i in words:
    if len(i)>len(longest):
        longest=i
print(f'longest word:{longest},lenght:{len(longest)}')'''

# for i in range(1,6):
#     print(i,end=' ') 

# for j in range(1,6):
#     print(j**2,end=' ')

# for i in range(1,11):
#     if i%2==0:
#         print(i,end =' ')

# total=0
# for i in range(1,11):
#     total+=i
#     # print(total)# print(total) inside loops means it will calculate total repeatedly every time   
# print(total)

#  writing a word in reverse order
'''w='python'
for i in range(len(w)-1,-1,-1 ):
    print(w[i],end='')'''

# counting no of vowels in word
'''c=0
w='Education'
for i in 'aeiou':
    if i.lower() in 'aeiou':
        c+=1
print(c)'''

'''a=0
b=1
# print(a,b)
for _ in range(8):
    next_term=a+b
    print(next_term)
    a,b=b,next_term'''

# factorial of a number
'''n=5
f=1
for i in range(1,n+1):
    f*=i
print(f)'''
    
# check if a no is prime or composite    
'''n=30
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print('prime')
if c>2:
    print('composite')'''

# a=1     
# while a<=15:
#     print(a,end=' ')
#     a+=1

# a=1
# while a<=5:
#     print(a**3,end=' ') 
#     a+=1

# a=1
# while a<=10:
#     if a%2!=0:
#         print(a,end=' ')
#     a+=1

# product of no from 1 to 5
# n=1     
# a=1
# while a<=5:
#     n*=a
#     a+=1
# print(n)

# reverse each word in a sentence
'''s='hello world'
words=s.split()
for word in words:
    i=len(word)-1
    while i>=0:
        print(word[i],end='')
        i-=1
    print(end=' ')'''

# count the no of consonents in word
'''w='learning'
c=0
i=0
while i<len(w):
    if w[i].lower() not in 'aeiou' and w[i].isalpha():
        c+=1
    i+=1
print(c)  '''

# i=1
# while i<=5:
#     print(3*i,end=' ')
#     i=i+1

# b=3
# e=4
# i=2
# while i<=e:
#     b=b**i
#     # i+=1
# print(b)

# square root of a number
# n=1
# while n<=16:
#     if n**2==16:
#         print(n)
#         break
#     n+=1

# counting the no of letter in string
'''s='success'
c=0
i=0
while i < len(s):
    if s[i]=='s':
        c+=1
    i+=1
print(c)'''
    
#  sum of even no till n 
# n=10
# sum=0
# for i in range(0,n+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)  

# using while loop
'''i=0
sum=0
while i<=10:
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)'''

# skip 5th iteration (multiple of 2 till 10)
'''n=2
for i in range(1,11):
    if i==5:
        continue
    print(f'{n}*{i}={n*i}')'''

# reversing a string using loop 
'''s='data science'
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1'''

'''s='data science'
idx=len(s)-1
for i in range(len(s)-1, -1, -1):
    print(s[i], end='')'''

# find first non repeated letter in string
'''strr='teetera'   # hard coded
for l in strr:
    if strr.count(l) == 1:
        print(l)
        break'''

# facotrial using while loop
'''f=1
n=5
while n>0:
    f=f*n
    n-=1
print(f) '''

#asking for input untill user enter a no between 1 and
'''while True:
    n=int(input('enter a num:'))
    if 1<=n<=10:
        print('yes no is b/w 1 and 10')
        break
    else:
        print('invalid no! try again')'''

# check if no is prime
'''n = int(input('enter a num:'))
if n <= 1:
    print('neither prime nor composite')
else:
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1

    if c == 2:
        print('prime')
    else:
        print('composite')'''

# reverse of an integer using loop
# n=str(1234)
# i=len(n)-1
# while i>=0:
#     print(n[i],end='')
#     i-=1

# count no of digits in integer using loop
# n=98765
# n=str(n)
# c=0
# for i in n:
#     c=c+1
# print(c)

# sum of digits of a number using loop
# n=123452
# summ=0
# for i in str(n):
#     i=int(i)
#     summ=summ+i
# print(summ)
    
# check if a no is palindrome or not using loop
'''n=121
original=n
reverse=0
while n != 0:
  digit=n%10
  reverse= 10*reverse+digit
  n=n//10
if original==reverse:
    print('palindrome')
else:
    print('not palindrome')
print('reverse of the number is : ',reverse)'''

# largest digit in an integer
'''n=126345
n=str(n)
largest=int(n[0])
for digits in (n):
    digits=int(digits)
    if digits>largest:
        largest=digits
print(largest)'''

# print all dividers of a no
'''n=100
dividers=set()
for i in range(1,n+1):
    if n%i==0:
        dividers.add(i)
print(f'dividers of {n} :',dividers) ''' 

# check if no is prime
'''n=11
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print('prime')
else:
    print('composite')'''
        
# sum of even digits
'''n=input('enter a number :')
sum_even=0
for i in n:
    i=int(i)
    if i%2==0:
        sum_even+=i
print(sum_even)'''

#  remove last digit repeatedly(stop when no become single digit)
'''n=1234
while n >= 10:
    # digits=n%10 # extract last digit
    n=n//10 # then remove the last digit
    # print(digits)
print(n)'''

# reverse a no
# n=1234
# reverse=0
# while n>0:
#     digit=n%10
#     n=n//10
#     reverse=reverse*10+digit
# print(reverse)

# largest digit
# n=1234
# largest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit>largest:
#      largest=digit
# print(largest)

# check palindrome
# n=121
# original=n
# reverse=0
# while n>0:
#      digit=n%10
#      n=n//10
#      reverse=reverse*10+digit
# if reverse==original:
#     print('palindrome')
# else:
#     print('not palindrome')

# product of digits
# n=98
# product=1
# while n>0:
#       digit=n%10
#       n=n//10
#       product*=digit
# print(product)

# count even digits
# n=123456
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit%2==0:
#         count+=1
# print(count)

#  check if no is amstrong no
# n=153
# original=n
# summ=0
# while n>0:
#        digit=n%10
#        n=n//10
#        summ=digit**3 + summ
# if summ==original:
#     print('yes no is amstrong no')
# else:
#     print('no is not amstrong no')

# remove specific digit from no and rebuild no without that digit
#  i could not solve

# second largest digit
# n=1234
# largest=0
# second_largest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit>largest:
#         second_largest=largest
#         largest=digit
#     elif digit<largest and digit>second_largest:
#         second_largest=digit
# print(second_largest)





    
    