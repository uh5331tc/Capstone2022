'''Noelle Bauer student.py'''


class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

alice = Student('Alice', 'aa2345ff', '3.33')
fred = Student('Fred', 'bb3333ss', '3.77')
sara = Student('Sara', 'kk3434oo', '3.88')

print(alice.name)
print(fred.college_id)
print(sara.gpa)