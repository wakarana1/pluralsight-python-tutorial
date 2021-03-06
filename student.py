students = []


class Student:

  school_name = "Springfield Elementary" #static variable/class attribute

  def __init__(self, name, student_id=332):
    self.name = name
    self.student_id = student_id
    students.append(self)
  # pass # do nothing

  def __str__(self): # overrides method in object
    return "Student"

  def get_name_capitalize(self):
    return self.name.capitalize()

  def get_school_name(self):
    return self.school_name
