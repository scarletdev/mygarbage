# Written by Scarlet

class Student:
    school_name = "ABC Lisesi" #class variable

    def __init__(self,name,age,grades):
        self.name = name #instance variable
        self.age = age
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)
    def schoolName(self):
        return f"studying at {self.school_name}"

student_1 = Student("Gordon",15,[64,24,52,71])
student_2 = Student("G-Man",45,[75,58,94,87])
student_3 = Student("Alyx",28,[85,10,65,90])

print(student_1.average())

print(student_1.schoolName())

print(student_1.__dict__)

"""GÖREV:
Student isimli bir class oluşturalım,
properties(attributes) 3 adet name, age, grades
methods 1 adet grades (notlar) ortalamasını gösteriyor
"""