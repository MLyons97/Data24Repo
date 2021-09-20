##Key and value pairs
##A few conditions:
##      Can't have repeated keys

student1 = {"name": "Susan",
            "stream":"tech",
            "completed_lessons":4,
            "lessons_completed_names":["Variables","Data Types","Disctionaries","Other"]
            }
print(student1["lessons_completed_names"])

student1["lessons_completed_names"].remove("Data Types")
print(student1["lessons_completed_names"])

print(list(student1.values())) ##This is its own data type, but can be cast into a list
