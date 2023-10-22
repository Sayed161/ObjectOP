import time
import math
class school:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
            self.teachers[subject] = teacher


    @staticmethod
    def calculate_grade(marks):
        if 80<= marks <= 100:
            return 'A+'
        elif 70 <= marks <= 80:
            return 'A'
        elif 60 <= marks <= 70:
            return 'A-'
        elif 50 <= marks <= 60:
            return 'B'
        elif 40 <= marks <= 50:
            return 'C'
        elif 33 <= marks <= 40:
            return 'D'
        else:
            return 'F'
        
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A' : 4.00,
            'A-': 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        
        return grade_map[grade]

    def student_admission(self,student):
        classname = student.classroom.name
        if classname in self.classrooms:
            #todo: set student id,(roll num),at the time of adding the student
            self.classrooms[classname].add_student(student)
        else:
            print(f"No class room name {classname}")

    def __repr__(self) -> str:
        print(10*'-'," ALL CLASSROOM ","-"*10)
        for key,value in self.classrooms.items():
            print(key) 
        
        print("-"*10," All STUDENTS ","-"*10)
        eight = self.classrooms['Eight']
        for student in eight.students:
            print(student.name)

        print(10*'-',end='')
        print(" ALL SUBJECTS ","-"*10)
        for subject in eight.subjects:
            print("Subject : ",subject.name," , Teacher : ",subject.teacher.name)
        
        print("-"*10," All STUDENTS MARKS ","-"*10)
        for student in eight.students:
            print(student.name)
            sum = 0
            for key,value in student.marks.items():
                sum+=value
                print(key,"-",value,student.subject_grade[key])   
            student.grade = sum/len(student.subject_grade)
            grade = school.calculate_grade(math.ceil(student.grade))
            print('-'*10,f'Final grade : ({grade})','-'*10,'\n\n',)
        return ""
class classroom:
    def __init__(self,name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self,student):
        Serial_id = f"{2023}-{self.name}-{len(self.students)+1}"
        student.id = Serial_id 
        self.students.append(student)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)


    def add_subject(self,subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'

    #todo: sort student by grade
    def get_topper(self):
        pass


class Subject :
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33
        
    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = school.calculate_grade(mark)
            