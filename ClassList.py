'''Noelle Bauer 8/25/2022 This program asks a user for the classes they are taking
and saves them to a list'''

#class_list = []
# GET user input 
class_names = input('What Classes are you taking this semester?')

class_list = class_names.split(' ')
#class_list.append(class_names)
#class_list.append(class_names.split())
#class_list.sort()

#looping to print one on each line 
for x in class_list:
    print(x)
