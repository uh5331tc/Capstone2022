"""Noelle Bauer Lab 1 Hello, Birthday Month This program asks a user for their birthday month"""
# get user input for name and birthday month 
name = input('What is your name?')
b_date = input('What month were you born in?')
print(f'Welcome {name}!!!')

#number of letters in the name 
name_length = len(name)

bDateGreeting = print('This month is your Birthday!')

#IF STATEMENTS 
if b_date == 'August' or 'august':
    print('Happy Birthday Month!!') #prints NONE
else:
    print(f'It is not your birthday month, your birthday is in {b_date}')

print(f'Your name is {name_length} characters long.')
print(f'You were born in {b_date}.')