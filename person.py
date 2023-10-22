import random
class Person:
    def __init__(self,name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)


    def teach(self):
        pass

    def __repr__(self) -> str:
        return f"{self.name}"



    def evaluate_exam(self):
            marks = random.randint(0,100)
            return marks
            # TODO:  Set marks for the subject for each student


class student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom = classroom 
        self.__id = None
        self.subjects = []
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

        

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id == value