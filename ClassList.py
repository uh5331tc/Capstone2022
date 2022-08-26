'''Noelle Bauer 8/25/2022 This program asks a user for the classes they are taking
and saves them to a list'''

# GET user input 
classes = []  #initialize an empty list for the class names to go

class_name = input('What Classes are you taking this semester?')

while class_name:
    classes.append(class_name)
    class_name = input('Enter a class name? or press ENTER to quit: ')

print(classes)

#looping to print one on each line 
for c in classes:
    print(c)

for index, c in enumerate(classes):
    print(f'{index+1}: {c}')
