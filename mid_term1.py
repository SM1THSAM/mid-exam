class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department
        self.__id = len(StudentDatabase.student_list) + 101
        self.__is_enrolled = False 

    def enroll_student(self):
        if not self.__is_enrolled:
            StudentDatabase.add_student(self)
            self.__is_enrolled = True
            print(self.__name, 'has been enrolled with ID:', self.__id)
        else :
            print(f'{self.__name} has been enrolled alrealdy with ID: {self.__id}')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(self.__name, 'has been dropped.')
        else :
            print('he has already been dropped')

    def view_student_info(self):
        return (f'Name: {self.__name}, Department: {self.__department}, ID: {self.__id}, Enrollment Status: {self.__is_enrolled}')

    def get_id(self):
        return self.__id

def shinobi_ats_school():
    print('-------------------Welcome to Shinobi Arts School------------------------')
    print('Here we teach the ancient arts of shinobi passed down from thousand years.') 
    print('1. View all students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    print('Enter 1,2,3,4 respectively for Viewing, Enrolling, Dropping, or Exiting.')

    rep = True
    while rep:
        try:
            response = int(input('Select option: '))
            if response == 1:
                if not StudentDatabase.student_list:
                    print('Studetnt database is Empty')
                else :
                    for index, student in enumerate(StudentDatabase.student_list, start=1):
                        print(f'sl no. {index} {student.view_student_info()}')
            elif response == 2:
                name = input('Name of the student: ')
                department = input('Desired department: ')
                student = Student(name, department)
                student.enroll_student()
            elif response == 3:
                ID = int(input('ID of the student to drop: '))
                found = False
                for student in StudentDatabase.student_list:
                    if student.get_id() == ID:
                        student.drop_student()
                        found = True
                        break
                if not found:
                    print("Student ID not found.")
            elif response == 4:
                print('Exiting the system...')
                rep = False
            else:
                print("Invalid option. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number.")

# student1 = Student('Ali', 'Mechanical')

shinobi_ats_school()
