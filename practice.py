'''Week 2 practice Python Basics'''

from datetime import datetime, date, time

#DAY OBJECT you can work with in programs
today = date.today()
print(today)

tomorrow = date(2022, 9, 1)  #ISO FORMAT
print(tomorrow)

next_week = date.fromisoformat('2022-09-01')  
print(next_week)


## time stamps  date.time
right_now = datetime.now()
print(right_now)
print(right_now.timestamp())  #number of seconds since  1/1/1970

#will use in sql lite where date time is not an existing object
#and then you can convert it into something readable
my_date = datetime.fromtimestamp('15000') #converts stamp into date object 
print(my_date)

#TUPLE once you create it you can't change it
city_state = [ ('Citya', 'statea'), ('cityb', 'stateb'), ('cityc', 'statec')]
print(len(city_state))  ## citya will always be with statea, so they will stay together

## get the first item in the list
first_city_state = city_state[0]  
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

## this will unpack the TUPLE into the followoing two variables
city, state = first_city_state
print(city)

##tuple unpacking, make sure you have enough variable to upack the values into
anmials = ('Lion', 'puma', 'tiger')
lion, puma, tiger = anmials
print(tiger)

## example function get distance
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km
distances = get_distance()
print(distances[0])

## OR TRY THIS
miles, km = get_distance()
print(km)


#SETS prevents duplicates order is never guarenteed
cats = set()  # creats new empty set
cats.add('Lion')
cats.add('Tigre')
print(cats)
cats.add('Cheetah')
print(cats)  #does not self order.

birds = { 'owl', 'robin', 'swan'}
print(birds)
birds.add('robin') #will not allow 'robin' to be added twice
print(birds)

birds.remove('owl')
birds.add('cardinal')
print(birds)

#looping over sets
for bird in birds:
    print(bird)

#remove duplicates from a list converting to set()
birds_list = ['owl', 'robin', 'swan', 'eagle', 'cardinal', 'swan', 'swan']
bird_list_no_duplicates = list(set(birds_list))
print(bird_list_no_duplicates) #will lose the ordering

##useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'tiger', 'stripes'  # returns a tuple

##unpack the TUPLE to conventiently get both values in seperate variable
cat, pattern = get_random_cat_and_pattern()
## error handing 
data = get_random_cat_and_pattern()

try:
    print(data[10])  #tiger
except:
    print('oopps that does not exist.')

