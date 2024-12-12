class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dob = ""

    def input(self):
        self.id = input('Enter Student ID: ')
        self.name = input('Enter name of Student: ')
        self.dob = input('Enter Date of birth of Student (dd-mm-yyyy): ')

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.mark = {}

    def input(self):
        self.id = input('Enter Course ID: ')
        self.name = input('Enter name of Course: ')

    def add_mark(self, studentID, mark):
        self.mark[studentID] = mark

    def get_mark(self, studentID):
        return self.mark.get(studentID)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Class:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        studentnumber = int(input('Enter number of student in your class: '))
        print(f"# of students in your class is: {studentnumber}")

        for _ in range(studentnumber):
            student = Student()
            student.input()
            self.students.append(student)
            print("Done!")

    def input_courses(self):
        coursenumber = int(input('Enter number of course: '))
        print(f"# of courses is: {coursenumber}")

        for _ in range(coursenumber):
            course = Course()
            course.input()
            self.courses.append(course)

    def list_students(self):
        print("Students list: ")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("Course list: ")
        for course in self.courses:
            print(course)

    def add_marks(self):
        print("\nAvailable courses:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.name} (ID: {course.id})")

        course_choice = int(input("\nSelect course to add marks: ")) - 1
        selected_course = self.courses[course_choice]

        print(f"\nStart entering marks for {selected_course.name}!")

        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} (ID: {student.id}): "))
            selected_course.add_mark(student.id, mark)

        print("Done!")

        print(f"\nMarks for {selected_course.id}:")
        for student in self.students:
            print(f"Student: {student.name}, Mark: {selected_course.get_mark(student.id)}")

def main():
    classroom = Class()
    classroom.input_students()
    classroom.list_students()
    classroom.input_courses()
    classroom.list_courses()
    classroom.add_marks()

if __name__ == "__main__":
    main()