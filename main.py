from student import Student
Lajos = Student("Lajos", 67, 178, "fiu")
anna = Student("Anna", 15, 170, "lány")
print(Lajos.name)
print(Lajos.height)
print(Lajos.age)
print(Lajos.gender)
print(Lajos.score)
Lajos.learn(10)

print(Lajos.introduce())
print(anna.introduce())
print(anna.score)