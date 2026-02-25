class Student:
    name = ""
    age = 0
    height = 0
    gender = ""
    score = 0

    def learn(self, test):
        self.score += test

    def __str__(self):
        return(f"{self.name}, {self.age}, {self.height}, {self.gender}, {self.score}")

Lajos = Student()
anna = Student()
print(Lajos)
Lajos.name = "Laci"
Lajos.age = 67
Lajos.height = 178
Lajos.gender = "fiu"
Lajos.score = 1
print(Lajos.name)
print(Lajos.height)
print(Lajos.age)
print(Lajos.gender)
print(Lajos.score)
Lajos.learn(10)

print(Lajos)
print(anna)