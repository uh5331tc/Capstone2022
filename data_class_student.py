'''Noelle Bauer student.py'''

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: str
    gpa: float

alice = Student('Alice', 'aa2345ff', '3.33')
print(alice.name)
print(alice.college_id)
print(alice.gpa)

fred = Student('Fred', 'bb3333ss', '3.77')
print(fred.name)
print(fred.college_id)
print(fred.gpa)

sara = Student('Sara', 'kk3434oo', '3.88')
print(sara.name)
print(sara.college_id)
print(sara.gpa)

# print(alice.name)
# print(fred.college_id)
# print(sara.gpa)