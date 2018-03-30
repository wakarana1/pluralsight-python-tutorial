students = []

def get_students_titlecase():
  students_titlecase = []
  for student in students:
    students_titlecase.append(student["name"].title())
  return students_titlecase


def print_student_titlecase():
  students_titlecase = get_students_titlecase()
  print(students_titlecase)


def add_student(name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)


student_list = get_students_titlecase()
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)

print_student_titlecase()


# NESTED FUNCTIONS
# def get_students():
#   students = ["mark", "james"]
#   def get_students_titlecase():
#     for student in students:
#       students_titlecase.append(student.title())
#     return students_titlecase
#   students_titlecase_names = get_students_titlecase()
#   print(students_titlecase_names)
