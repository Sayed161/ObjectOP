from school import *
from person import *
def main():
    School = school("Adam je ","Uttara")
    eight = classroom("Eight")
    School.add_classroom(eight)
    nine = classroom("Nine")
    School.add_classroom(nine)
    Ten = classroom("Ten")
    School.add_classroom(Ten)


    Abir = student("Abir Khan",eight) 
    School.student_admission(Abir)
    Jubair = student("Jubair Khan",eight) 
    School.student_admission(Jubair)
    sohel = student("sohel Khan",eight) 
    School.student_admission(sohel)

    physics_Teacher = Teacher('Sheikh Rony')
    physics = Subject("Physics",physics_Teacher)
    eight.add_subject(physics)

    Math_Teacher = Teacher('Badshah')
    Math = Subject("Math",Math_Teacher)
    eight.add_subject(Math)
    
    Biology_Teacher = Teacher('Azmal')
    Biology = Subject("Biology",Biology_Teacher)
    eight.add_subject(Biology)

    eight.take_semester_final()
     
    

    print(School)









if __name__ == "__main__":
    main()