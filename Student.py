#creating a CLASS
class Student:
    
    #class Variable
    grade = 8
    print(f"I am a student of Grade {grade}")
    
    #creating Constructor Method(Method is a function that is inside of class)
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#Creating OBJECT
junaira = Student("Junaira", 12)
kashfia = Student("Kashfia",15)
rifa = Student("Rifa",14)

print(f"Name: {junaira.name}\nAge: {junaira.age}\n\n")
print(f"Name: {kashfia.name}\nAge: {kashfia.age}\n\n")
print(f"Name: {rifa.name}\nAge: {rifa.age}\n\n")

print(f"\n\nJunaira Grade: {junaira.grade}")
print(f"\n\nKashfia Grade: {kashfia.grade}")
print(f"\n\nRifa Grade: {rifa.grade}")