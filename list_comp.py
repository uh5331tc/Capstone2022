#the classes a student is registered for 
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ITEC 2950', 'MATH 5000']

# make a list of only the ITEC Classes from the classes_registered list
#only_itec = [ c.lower for c in classes_registered] #lower case
#only_itec = [ c for c in classes_registered if c.startswith('ITEC')] #gets jsut the ITEC Classes

only_itec = [ c for c in classes_registered] 
print(only_itec)


# record tempretures eery day. record -1 if none taken that day
high_temps = [-2, 78, 72, 87, 67, -1, 78, 80, -1, 88]

#make a list of only days you recorded (does not include -1 temps)
only_real_temps = [temp for temp in high_temps if temp != -1]
print(only_real_temps)

temp_celsius = [ (temp_f -32) * 5 / 9 for temp_f in only_real_temps ]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is  + {average:.2f} Degrees Celsius')  #.2f decimal placing

# LIST COMPREHENSION SYNTAX
#make a list from another list
strings = ['pizza', 'Beyonce', 'dog']
lenghts = []

for string in strings:
    length = len(string)
    lenghts.append(length)
print(lenghts)

#how to convert string item in new list  and how to loop over the list
strings = ['pizza', 'Beyonce', 'dog']
lenghts = [len(string) for string in strings]
print(lenghts)

#list comprehension that increases each list item by ONE
numbers = [ 2,4,6]
plus_one = [n+1 for n in numbers]
print(plus_one)

## can add a condition to filter the list
numbers = [1, -10, 40, 34, 203, -34]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers)

foods = ['bread', 'meat', 'veggies']
sandwhiches = [food for food in foods if 'bread' in food]
print(sandwhiches)

##remember python does not do .contains() methods, you need to use
## the    in    operator to see if a string contains a substring, or a 
## list contains an item

numbers = [0, 3, 6, 34, 666, 6, 0 ,0]
numbers_no_zeros = [ n for n in numbers if n != 0]
print(numbers_no_zeros)


# if the number is not equal to 0, double the number
numbers_doubled_no_zeros = [ n * 2 for n in numbers if n != 0 ]
print(numbers_doubled_no_zeros)





