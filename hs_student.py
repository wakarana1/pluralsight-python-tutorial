class HighSchoolStudent(Student): # HighSchoolStudent inherits from Student class
  """docstring for HighSchoolStudent"""

  school_name = "Springfield High School"

  def get_school_name(self):
    return "this is a high school student"

  def get_name_capitalize(self):
    original_value = super().get_name_capitalize() #inherits from student class
    return original_value + "-HS"
