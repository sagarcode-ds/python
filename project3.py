# Dictionary And Set
# Project 1: Student Gradebook (Dictionary of Scores)
'''Create a program that manages grades for 3 students.
1. Create an empty dictionary grades.
2. Ask for 3 student names and their scores (store as name: score).
3. Display the dictionary.
4. Ask for a student name to look up their score (use .get() with a friendly message if not found).
5. Ask for a student name to update their score (update directly).
6. Find and display:
   · Student with highest score (compare values manually)
   · Average score (add values and divide by 3)
7. Display all students who scored above 75 (check each manually).'''
'''grades={}
name1=input('enter first student name:')
score1=int(input('enter first student score :'))
name2=input('enter second student name:')
score2=int(input('enter second student score :'))
name3=input('enter third student name:')
score3=int(input('enter third student score :'))
grades.update({name1:score1})
grades.update({name2:score2})
grades.update({name3:score3})
print('Student Names And Grades :',grades)
# name='riya'
# After creating and displaying the grades dictionary
name = input("Enter student name to look up: ")

if(name in grades): # upcoming concept loop
    print(f"{name}'s score: {grades[name]}")
else:
    print(f"Student '{name}' not found in database")
change=input('enter student name to update score :')
new_score=int(input(f'enter updated score of {change} :'))
grades[change]=new_score
print('Updated dictionary:',grades)
highest = grades[name1]  # Start with first
if grades[name2] > highest:
    highest = grades[name2]
if grades[name3] > highest:
    highest = grades[name3]
print('Highest Score :',highest)
print('Average Score :',round((grades[name1]+grades[name2]+grades[name3])/len(grades),2))
print('Students who scored above 75 are given below')
print('-'*40)
if(grades[name1]>75):
    print(f"{name1}:{grades[name1]}")
if(grades[name2]>75):
    print(f"{name2}:{grades[name2]}")
if(grades[name3]>75):
    print(f"{name3}:{grades[name3]}")
print('-'*40)'''

# Project 2: Phone Book with Multiple Numbers (Dictionary of Lists)
'''Create a phone book where each contact can have multiple phone numbers.
1. Create an empty dictionary contacts.
2. For 2 contacts:
   · Ask for name
   · Ask for 2 phone numbers (store as a list)
   · Add to dictionary as name: [phone1, phone2]
3. Display the phone book.
4. Ask for a name to look up — show their numbers (use .get()).
5. Ask for a name to add a third number to — append to their list.
6. Display updated phone book.'''
# note: keep phone no as string
'''contacts={}
name1=input('enter first name:')
phone_1a=(input('enter phone 1a:'))  
phone_1b=(input('enter phone 1b:'))
phone1=[phone_1a,phone_1b]
name2=input('enter second name:')
phone_2a=(input('enter phone 2a:'))
phone_2b=(input('enter phone 2b:'))
phone2=[phone_2a,phone_2b]
contacts.update({name1:phone1})
contacts.update({name2:phone2})
print('Phone Book :',contacts)
name=input('enter name to look up :')
if name in contacts:
    print(f'{name} phone no are:',contacts.get(name))
else:
    print(f" the name {name} is not present in contacts")
add_name=input('enter name to add third no:')
add_no=input('enter no to add:')
if add_name in contacts:
    contacts[add_name].append(add_no)
    print('Updated Phone Book :',contacts)
else:
    print(f'the name {add_name} not found in contacts')'''

# Project 3: Word Characteristics Dictionary
'''Topics: Dictionary with multiple value types, string methods, tuple as key (optional)
Create a program that analyzes 3 words and stores multiple properties for each.
1. Ask for 3 words.
2. For each word, create a dictionary with:
   · 'length': length of word
   · 'vowels': count of vowels (a,e,i,o,u)
   · 'first': first character
   · 'last': last character
   · 'is_palindrome': True/False (word == word[::-1])
3. Store all 3 word dictionaries inside a main dictionary with the word as key.
4. Display the complete nested dictionary.
5. Ask for a word to look up — print all its characteristics.
6. Find which word has the most vowels (compare manually).'''
'''word1=input('enter 1st word :')
word2=input('enter 2nd word :')
word3=input('enter 3rd word :')
print('-'*49)
vowel1=word1.lower().count('a')+word1.lower().count('e')+word1.lower().count('i')+word1.lower().count('o')+word1.lower().count('u')
vowel2=word2.lower().count('a')+word2.lower().count('e')+word2.lower().count('i')+word2.lower().count('o')+word2.lower().count('u')
vowel3=word3.lower().count('a')+word3.lower().count('e')+word3.lower().count('i')+word3.lower().count('o')+word3.lower().count('u')
word={
    word1:{
        'length':len(word1),
        'no of vowels':vowel1,
        'first character':word1[0],
        'last character':word1[-1],
        'is palindrome':word1==word1[::-1]},
    word2:{
        'length':len(word2),
        'no of vowels':vowel2,
        'first character':word2[0],
        'last character':word2[-1],
        'is palindrome':word2==word2[::-1]},
    word3:{
        'length':len(word3),
        'no of vowels':vowel3,
        'first character':word3[0],
        'last character':word3[-1],
        'is palindrome':word3==word3[::-1]}}
print('Complete Nested Dictionary :',word)
print('-'*49)
lookup=input('enter a word to lookup in dictionary:')
if lookup in word:   # corrected(most important)
    print(f"Characteristics of '{lookup}':")
    print(f"Length: {word[lookup]['length']}")
    print(f"Vowels: {word[lookup]['no of vowels']}")  
    print(f"first word: {word[lookup]['first character']}")
    print(f"last word: {word[lookup]['last character']}")
    print(f"is palindrome ?:{word[lookup]['is palindrome']}")
else:
    print('invalid word !!')  
print('-'*49)
most_vowel=word1  # corrected
max_vowel=vowel1 # note that max vowel is also needed
if vowel2>max_vowel :
    most_vowel=word2
    max_vowel=vowel2
if vowel3>max_vowel:
    most_vowel=word3
    max_vowel=vowel3
print('word with most vowels :',most_vowel)
print(f"no of vowels in {most_vowel}:",max_vowel)'''

# Project 4: Set Operations on Two Groups
'''Topics: Set creation, union, intersection, difference, subset check
Create a program that works with two sets of students.
1. Ask for 4 students in "Math Club" (store in a set).
2. Ask for 4 students in "Chess Club" (store in a set).
3. Display both sets.
4. Find and display:
   · Students in both clubs (intersection: set1 & set2)
   · Students in either club (union: set1 | set2)
   · Students only in Math Club (difference: set1 - set2)
   · Students only in Chess Club (difference: set2 - set1)
5. Ask for a student name and check if they're in Math Club (use in).
6. Check if Math Club is a subset of Chess Club (use <=).'''
'''name1=input('enter 1st student name in math club:')
name2=input('enter 2nd student name in math club:')
name3=input('enter 3rd student name in math club:')
name4=input('enter 4th student name in math club:')
set1={name1,name2,name3,name4}
print('Students in math club:',set1)
name5=input('enter 1st student name in chess club:')
name6=input('enter 2nd student name in chess club:')
name7=input('enter 3rd student name in chess club:')
name8=input('enter 4th student name in chess club:')
set2={name5,name6,name7,name8}
print('Students in chess club:',set2)
print('Students in both club:',set1.intersection(set2))
print('Students in either club:',set1.union(set2))
print('Students only in math club:',set1-set2)
print('Students only in chess club:',set2-set1)
name=input("is name in math club ? :")
if name in set1:
    print(f'\n{name} is in math club')
else:
    print(f'\n{name} is not in math club')
if set1 <= set2:
    print("\nyes math club is subset of chess club")
else:
    print("\nno math club is not subset of chess club")'''

# Project 5: Inventory with Categories (Dictionary of Sets)
'''Topics: Dictionary with sets as values, adding/removing, set operations
Create an inventory system where items are organized by category.
1. Create a dictionary inventory with 3 categories: 'fruits', 'vegetables', 'drinks' — each with an empty set.
2. For each category, ask for 3 items to add to that category's set.
3. Display all categories and their items.
4. Ask for a category to add one more item to.
5. Ask for an item to search for — check which categories contain it (check each set manually using in).
6. Find and display items that appear in multiple categories (use set intersections manually).'''
# writing input would take time so i just hard coded
'''inventory={'fruits':set(),'vegetables':set(),'drinks':set()}
item1='apple'
item2='banana'
item3='mango'
inventory['fruits'].add(item1)
inventory['fruits'].add(item2)
inventory['fruits'].add(item3)
item4='potato'
item5='tomato'
item6='spinach'
inventory['vegetables'].add(item4)
inventory['vegetables'].add(item5)
inventory['vegetables'].add(item6)
item7='water'
item8='beer'
item9='coca cola'
inventory['drinks'].add(item7)
inventory['drinks'].add(item8)
inventory['drinks'].add(item9)
print('inventory system :',inventory)
category='fruits'
add_item='orange'
if category in inventory:
    inventory[category].add(add_item)
    print('\nUpdated Inventory System:',inventory)
else:
    print(f"{category} is not in inventory !!")
search_item='apple'
if search_item in inventory['fruits']:
    print(f"\n{search_item} is in category fruits") 
elif search_item in inventory['vegetables']:
    print(f"\n{search_item} is in category vegetables")
elif search_item in inventory['drinks']:
    print(f"\n{search_item} is in category drinks")
else: 
    print(f'\ninvalid item!! {search_item} is not in any category.')
# following part is copy pasted
fruits_veg = inventory['fruits'] & inventory['vegetables']
fruits_drinks = inventory['fruits'] & inventory['drinks']
veg_drinks = inventory['vegetables'] & inventory['drinks']
multiple_categories = fruits_veg | fruits_drinks | veg_drinks
print("\nItems in multiple categories:", multiple_categories)'''

# Project 6: Voting System with Multiple Rounds (Dictionary of Counts)
'''Topics: Dictionary with counts, updating values, finding max
Create a simple voting system for 3 candidates across 2 voting rounds.
1. Create a dictionary votes with candidates 'Alice', 'Bob', 'Charlie' — each starting with 0 votes.
2. Round 1: Ask 3 voters to vote (each enters a candidate name). Update counts.
3. Display round 1 results.
4. Round 2: Ask 3 more voters to vote. Update counts.
5. Display final results.
6. Determine the winner (candidate with highest total votes) — compare manually.
7. Check if any candidate got zero votes in either round (you'll need to track round-wise votes separately or use two dictionaries).'''

'''votes={'alice':0,
        'bob':0,
        'charlie':0}
# round1:  #note:(vote1,0) if vote1 is not in votes,then 0 vote is added by default
vote1='alice'
vote2='bob'
vote3='charlie'
votes[vote1]=votes.get(vote1,0)+1
votes[vote2]=votes.get(vote2,0)+1
votes[vote3]=votes.get(vote3,0)+1
print('Round 1 Result :',votes)
# round2:
vote4='alice'
vote5='bob'
vote6='bob'
votes[vote4]=votes.get(vote4,0)+1
votes[vote5]=votes.get(vote5,0)+1
votes[vote6]=votes.get(vote6,0)+1
print('\nFinal Result :',votes)
max_candidate='alice'
max_votes=votes['alice']
if votes['bob'] > max_votes:
    max_votes=votes['bob']
    max_candidate='bob' 
if votes['charlie'] > max_votes:
    max_votes=votes['charlie']
    max_candidate='charlie' 
print(f"\ncandidate with highest votes:{max_candidate},no of votes:{max_votes}")
# round1={'alice':votes[vote1],'bob':votes[vote2],'charlie':votes[vote3]}'''

# Round 2
# Project 1: Product Catalog with Nested Dictionaries
'''Topics: Nested dictionaries, dictionary access, manual comparison, basic arithmetic
Create a product catalog where each product has a nested dictionary of details.
1. Ask for 3 products. For each, get:
   · Product name
   · Price
   · Quantity in stock
   · Category (e.g., "electronics", "clothing", "food")
2. Store all products in a main dictionary catalog with product name as key and a nested dictionary as value:
      catalog[name] = {'price': price, 'qty': qty, 'category': category}
3. Display the catalog in a neat format.
4. Find and print:
   · Most expensive product (compare prices manually)
   · Total inventory value (sum of price × qty for each product)
   · Products in a specific category (ask user for category, then check each product's category manually)
5. Ask for a product name to update its quantity (new value) — update the dictionary.
6. Ask for a category and calculate total value of products in that category.'''
'''name1='mobile'
price1=200
quantity1=12
category1='electronics'
name2='T-shirt'
price2=280
quantity2=10
category2='clothing'
name3='rice'
price3=340
quantity3=22
category3='food'
catalog={
    name1:{'price':price1,'quantity':quantity1,'category':category1},
    name2:{'price':price2,'quantity':quantity2,'category':category2},
    name3:{'price':price3,'quantity':quantity3,'category':category3}
}
print('Catalog :',catalog)
most_expensive=catalog[name1]['price']
most_ex_product=name1
if catalog[name2]['price'] > most_expensive:
    most_expensive=catalog[name2]['price']
    most_ex_product=name2
if catalog[name3]['price'] > most_expensive:
    most_expensive=catalog[name3]['price']
    most_ex_product=name3
print(f'\nMost expensive product : {most_ex_product} with price {most_expensive}.')
total1=catalog[name1]['price']*catalog[name1]['quantity']
total2=catalog[name2]['price']*catalog[name2]['quantity']
total3=catalog[name3]['price']*catalog[name3]['quantity']
print('\nTotal Inventory Value :',total1+total2+total3)
ask_product='rice'
category=catalog[ask_product]['category']
print(f'\ncategory of {ask_product}: {category}')
ask_name='mobile'
new_quantity=32
# catalog.update({ask_name['quantity']:new_quantity})
catalog[ask_name].update({'quantity': new_quantity}) # or
catalog[ask_name]['quantity'] = new_quantity # both ways are correct
print('\nUpdated dictionary :',catalog)
ask_category='electronics'
if catalog[name1]['category'] == ask_category:
    print(f"Total value of product in {ask_category} :",catalog[name1]['price']*catalog[name1]['quantity'])
if catalog[name2]['category'] == ask_category:
    print(f"Total value of product in {ask_category} :",catalog[name2]['price']*catalog[name2]['quantity'])
if catalog[name3]['category'] == ask_category:
    print(f"Total value of product in {ask_category} :",catalog[name3]['price']*catalog[name3]['quantity'])
# note that we did not simply write total1,total2,total3 because product quantity was updated later'''

# Project 2: Character Frequency Analyzer (Fixed‑Length Word)
'''Topics: Dictionary for frequency counts, string indexing, .get() method
Write a program that analyzes a 5‑letter word (you can ask for a word and validate length if needed, but for simplicity assume user enters exactly 5 letters).
1. Ask for a 5‑letter word.
2. Create an empty dictionary freq.
3. For each position (0 to 4), manually add to frequency:
   · Get the character at that index.
   · Update count using freq[char] = freq.get(char, 0) + 1 — but you'll write this line 5 times, each with a different character variable.
4. Display the frequency dictionary.
5. Find and print:
   · Most frequent character (compare values manually)
   · Characters that appear more than once
   · Number of unique characters (len(freq))
6. Check if the word is an isogram (all characters unique — if len(freq) == 5).'''
'''word='sagar'
freq={}
letter1=word[0]
letter2=word[1]
letter3=word[2]
letter4=word[3]
letter5=word[4]
freq[word[0]]=freq.get(word[0],0)+1
freq[word[1]]=freq.get(word[1],0)+1
freq[word[2]]=freq.get(word[2],0)+1
freq[word[3]]=freq.get(word[3],0)+1
freq[word[4]]=freq.get(word[4],0)+1
print(' frequency dictionary :',freq)
print(f"\nfrequency : {letter1}:{freq[word[0]]},{letter2}:{freq[word[1]]},{letter3}:{freq[word[2]]},{letter4}:{freq[word[3]]},{letter5}:{freq[word[4]]}")
m_frequent=letter1
m_frequency=freq[word[0]]
if freq[word[1]] > m_frequency:
    m_frequency=freq[word[1]]
    m_frequent=letter2
if freq[word[2]] > m_frequency:
    m_frequency=freq[word[2]]
    m_frequent=letter3
if freq[word[3]] > m_frequency:
    m_frequency=freq[word[3]]
    m_frequent=letter4
if freq[word[4]] > m_frequency:
    m_frequency=freq[word[4]]
    m_frequent=letter5
print(f"\nmost frequent letter:{m_frequent} with frequency {m_frequency} ")
frequency=set()
if freq[word[0]] > 1:
    frequency.add(letter1)
if freq[word[1]] > 1:
    frequency.add(letter2)
if freq[word[2]] > 1:
    frequency.add(letter3)
if freq[word[3]] > 1:
    frequency.add(letter4)
if freq[word[4]] > 1:
    frequency.add(letter5)
print('\ncharacters that appears more than once :',frequency)
print('\nno of unique characters :',len(freq))
if len(freq) == 5:
    print(f'\nyes the word {word} is an isogram')
else:
    print(f'\nno the word {word} is not an isogram')'''

# Project 3: Set Operations on Three Friend Groups
'''Topics: Sets, union, intersection, difference, superset/subset checks
Create three sets of friends who like different sports:
· football fans
· basketball fans
· tennis fans
1. Ask for 3 names for each set (total 9 inputs). Build three sets.
2. Display each set.
3. Find and print:
   · People who like all three sports (intersection of all three: f & b & t — but you must compute stepwise: all_three = football & basketball; all_three & tennis)
   · People who like exactly two sports (you'll need to compute pairwise intersections and subtract the triple intersection manually — but you can do this with set operations)
   · People who like only football (football - basketball - tennis using - operator)
   · Total unique people across all sports (union of all three)
4. Ask for a name and check which sports they like (check membership in each set manually).
5. Check if the football set is a subset of the union of basketball and tennis (use <=).'''
'''name1='sagar'
name2='tyson'
name3='riya'
football={name1,name2,name3}
name4='sagar'
name5='priya'
name6='tyson'
basketball={name4,name5,name6}
name7='sagar'
name8='priya'
name9='raj'
tennis={name7,name8,name9}
print('Football fans :',football)
print('basketball fans :',basketball)
print('tennis fans :',tennis)
f_b=football & basketball 
f_b_t=f_b & tennis
print('\npeople who like all three sports :',f_b_t)
f_b=football & basketball
b_t=basketball & tennis
t_f=tennis & football
any_two=f_b | b_t | t_f
exactly_two=any_two-f_b_t
print('people who like exactly two soports :',exactly_two)
print('people who like only football :',football-basketball-tennis)
print('total unique people across all sports :',football|basketball|tennis)
name='sagar'
if name in football: 
    print(f"\n{name} like football")
if name in basketball: 
    print(f"\n{name} like basketball")
if name in tennis: 
    print(f"\n{name} like tennis")

if football <= (basketball | tennis):
    print('\nyes,football set is subset of union of basketball and tennis')
else:
    print('\nno,football set is not subset of union of basketball and tennis')'''

# Project 4: Two‑Round Voting with Elimination
'''Topics: Dictionary for vote counts, manual comparison, eliminating lowest
Simulate a simple election with 3 candidates: "Alice", "Bob", "Charlie".
Two rounds: if no one gets majority (>50%) in first round, eliminate the lowest candidate and hold a second round with the remaining two.
1. Initialize votes dictionary with all candidates at 0.
2. Round 1: Ask 5 voters to vote (each enters a candidate name). Update counts manually (5 separate inputs).
3. Display round 1 results.
4. Calculate total votes (5). If any candidate has >2.5 (i.e., ≥3) votes, declare winner. Else:
   · Find candidate with fewest votes (compare manually). If tie for lowest, you can pick any (or ask user to decide — simplify by picking first encountered).
   · Eliminate that candidate (remove from dictionary or just ignore).
   · Round 2: Ask the same 5 voters to vote again (you can just input 5 new votes). But this time, if they vote for eliminated candidate, count it as invalid? Better to just have them vote for remaining candidates.
   · Update counts for remaining candidates.
   · Display round 2 results and declare winner (candidate with more votes).'''

'''vote={'alice':0,'bob':0,'charlie':0}
# round 1 (assume each hard coded part as input)
vote1='alice'
vote2='bob'
vote3='charlie'
vote4='alice'
vote5='bob'
vote[vote1] +=1
vote[vote2] +=1
vote[vote3] +=1
vote[vote4] +=1
vote[vote5] +=1
print('round 1 result :',vote)
print('total votes :',vote['alice']+vote['bob']+vote['charlie'])
r1_votes=[vote['alice'],vote['bob'],vote['charlie']]
if vote['alice']>=3: #(2.5 = majority)
    print('winner:alice!') 
elif vote['bob']>=3:
    print('winner:bob!') 
elif vote['charlie']>=3:
    print('winner:charlie!') 
else:
    lowest_candidate = 'alice'   # corrected part
    lowest_votes = vote['alice']
    if vote['bob'] < lowest_votes:
        lowest_candidate = 'bob'
        lowest_votes = vote['bob']
    if vote['charlie'] < lowest_votes:
        lowest_candidate = 'charlie'
        lowest_votes = vote['charlie']
# Remove ONLY that one candidate
vote.pop(lowest_candidate)
print('remaining candidates :',vote)
# round 2:again assume each hard coded part as input
vote6='alice'
vote7='alice'
vote8='bob'
vote9='alice'
vote10='bob'
if vote6 in vote:  # corrected(2) if someone votes for eliminated candidate,it won't count
    vote[vote6] +=1
if vote7 in vote:
    vote[vote7] +=1
if vote8 in vote:
    vote[vote8] +=1
if vote9 in vote:
    vote[vote9] +=1
if vote10 in vote:
    vote[vote10] +=1
print('round 2 votes :',vote)
r2_votes=[vote['alice'],vote['bob']]
if max(r2_votes)==vote['alice']:
    print('winner:alice!')
if max(r2_votes)==vote['bob']:
    print('winner:bob!')'''

# Project 5: Weighted Grade Calculator for Multiple Students
'''Topics: Nested dictionaries, arithmetic, manual comparison
Create a gradebook for 3 students where each student has scores in multiple categories with different weights.
Categories: Homework (weight 30%), Quiz (20%), Exam (50%).
For each student, you'll store scores in a nested dictionary:
grades[student] = {'hw': hw_score, 'quiz': quiz_score, 'exam': exam_score}
1. Ask for names of 3 students.
2. For each student, ask for homework score (0-100), quiz score, exam score. Store in the nested dict.
3. Calculate final weighted grade for each student:
      final = hw*0.3 + quiz*0.2 + exam*0.5
4. Display each student's scores and final grade.
5. Find and print:
   · Student with highest final grade
   · Average final grade of all students
   · Students who passed (final ≥ 60)
6. Ask for a student name and print their detailed scores.'''
# assume each hard coded scores as input
name1='sagar'
name2='tyson'
name3='micheal'
h1=80 # h,q,e = homework score,quiz score,exam score respectively
h2=70
h3=60
q1=60
q2=70
q3=80
e1=70
e2=60
e3=80
