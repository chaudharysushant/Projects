class student:
    def __init__(self, name):
        self.name = name
        self._grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        

    def get_average(self):
        if not self._grades:
            return 0
        return sum(self._grades)/len(self._grades)
    
    def get_grades(self):
        return self._grades
    
s = student("ram")
s.add_grade(90)
s.add_grade(80)

print(s.name)
print(s.get_average())
print(s.get_grades())