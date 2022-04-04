from typing_extensions import Self


class Student:
    def __init__(self,name,cohort):
        self.name = name
        self.cohort = cohort
        
    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"

Student.name = "Mike"

Student.cohort = "G21"

 

