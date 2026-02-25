class Student:
    score = 0

    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.score = 0

    def learn(self, test):
        self.score += test

    def introduce(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old"

    def __str__(self):
        return(f"{self.name}, {self.age}, {self.height}, {self.gender}, {self.score}")