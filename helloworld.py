print('Hello World')

#single line comment
"""Multi line comment"""

# FORMAT FUNCTION
name = "Chris"
machine = "Hal"
print("Nice to meet you {0}, I am {1}".format(name, machine))

#string interopolation
f"Nice to meet you {name}, I am {machine}."

#LISTS

student_names = ["Mark", "Katrina", "Jessica", "Bort", "Frank", "Max"]
student_names.append("Homer")
print(student_names)

"Mark" in student_names #checks if Mark is in Array
len(student_names) #checks length of array
del student_names[1] #deletes from array

student_names[1:-1] # "katrina", "Max"

# FOR LOOPS

for name in student_names:
  if "Bort":
    print("found: " + name)
    break
  if "Jessica":
    continue
    print("Hello " + name) # will skip over
  print("currently testing: " + name)

# WHILE LOOPS

x = 0

while x < 10:
  print("Count is {0}".format(x))
  x += 1

# DICTIONARIES similar to JSON objects

student = {
  "name": "Mark",
  "student_id": 105,
  "feedback": None
}

student["name"] # "Mark"
student.keys # "name" "student_id" "feedback"
student.values #"Mark", 105, None

#List of dictionaries
all_students = [
  {"name": "Josh", "student_id": 10 },
  {"name": "Percy", "student_id": 35},
  {"name": "Tom", "student_id": 100 },
]

# EXCEPTION HANDLING
# Try except log

try:
  last_name = student["last_name"]
  numbered_last_name = 3 + last_name
except KeyError:
  print("Error finding last name")
except TypeError as error:
  print("I can't add these two together")
  print(error) #prints error
except Exception:
  print("Unknown Error")

# tuple == immutable lists
tuple = (1, 3, 5, "Mark")






