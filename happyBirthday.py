"""Noelle Bauer Lab 1 Hello, Birthday Month This program asks a user for their birthday month"""
from datetime import date


# get user input for name and birthday month 
name = input('What is your name?')
b_date = input('What month were you born in?')
print(f'Welcome {name}!!!')

#number of letters in the name 
name_length = len(name)

#IF STATEMENTS 
if b_date.lower() == 'august':
    print('Happy Birthday Month!!') 
else:
    print(f'It is not your birthday month, your birthday is in {b_date}')

print(f'Your name is {name_length} characters long.')
#print(f'You were born in {b_date}.')


# current date 
# at the top import date like this:
#       from datetime import date
now = date.today()
current_month = now.month  #if august it will be an 8

current_month = now.strftime('%B')