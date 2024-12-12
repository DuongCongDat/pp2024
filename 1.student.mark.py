studentnumber = int(input('Enter number of students in your class: '))
print(f'# students is: {studentnumber} ')

students = []
def add_student():
    studentID = input('Enter ID of student: ')
    studentName = input('Enter name of student: ')
    studentDoB = input('Enter student date of birth (dd-mm-yyyy): ')

    student = {
        'ID' : studentID,
        'Name' : studentName,
        'DoB' : studentDoB
    }

    students.append(student)
    print('Done!')

for __ in range(studentnumber):
    add_student()

print('\nStudents list: ')
for student in students:
    print(student)

coursenumber = int(input('\nEnter number of courses: '))
print(f'# course is: {coursenumber} ')

courses = []
def add_course():
    courseID = input('Enter ID of course: ')
    courseName = input('Enter name of course: ')

    course = {
        'ID' : courseID,
        'Name Course' : courseName
    }

    courses.append(course)
    print('Done!')

for __ in range(coursenumber):
    add_course()

print('\nCourses list: ')
for course in courses:
    print(course)


def add_marks():
    print("\n Available courses: ")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['Name Course']} (ID: {course['ID']})")

    course_choice = int(input("\n Select course to add marks: ")) - 1           #do o tren de i+1
    select_course = courses[course_choice]

    marks = {}
    print(f"\nStart enter mark for {select_course['Name Course']}! ")

    for student in students:
        mark = float(input(f"Enter mark for student {student['Name']} (ID: {student['ID']}): "))
        marks[student['ID']] = mark

    select_course['Marks'] = marks
    print("Done!")

    print(f"\nMark for {select_course['ID']}: ")
    for student in students:
        print(f"Student: {student['Name']}, Mark: {select_course['Marks'][student['ID']]}")

add_marks()