#Creating a CLASS
class Dog:
    #class variable
    age = int(input("Please enter a number upto 6: "))
    print(f"All dogs are {age} years old")
    
    #Creating Constructor Method(Method is a function that is inside of class)
    def _init_(self,name,color,breed,angerlevel,training_ability):
        self.name = name
        self.color = color
        self.breed = breed
        self.angerlevel = angerlevel
        self.training_ability = training_ability
    
#Creating OBJECT
buddy = Dog("Buddy", "Black", "Labrador Retriever", "calm", "highly trainable")
bella = Dog("Bella", "Black and Red", "German Shepherd", "confident", "military roles")
max2 = Dog("Max", "Golden", "Golden Retriever", "gentle", "High Intelligence")
charlie = Dog("Charlie", "Silver", "Poodle", "low", "Quick Learners")
luna = Dog("Luna", "White", "Bulldog", "Protective", "Stubbornness")

#For OUTPUT(Constructor)
print(f"Name = {buddy.name}\nColor = {buddy.color}\nBreed = {buddy.breed}\nAnger Level = {buddy.angerlevel}\nTraining ability = {buddy.training_ability}\n\n")


print(f"Name = {bella.name}\nColor = {bella.color}\nBreed = {bella.breed}\nAnger Level = {bella.angerlevel}\nTraining ability = {bella.training_ability}\n\n")


print(f"Name = {max2.name}\nColor = {max2.color}\nBreed = {max2.breed}\nAnger Level = {max2.angerlevel}\nTraining ability = {max2.training_ability}\n\n")


print(f"Name = {charlie.name}\nColor = {charlie.color}\nBreed = {charlie.breed}\nAnger Level = {charlie.angerlevel}\nTraining ability = {charlie.training_ability}\n\n")


print(f"Name = {luna.name}\nColor = {luna.color}\nBreed = {luna.breed}\nAnger Level = {luna.angerlevel}\nTraining ability = {luna.training_ability}\n\n")

#For OUTPUT(Class)
print(f"\n\nBuddy age = {buddy.age}")
print(f"\n\nBella age = {bella.age}")
print(f"\n\nMax age = {max2.age}")
print(f"\n\nCharlie age = {charlie.age}")
print(f"\n\nLuna age = {luna.age}")