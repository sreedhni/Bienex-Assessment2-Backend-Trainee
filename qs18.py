# 18. Python program to for student height record for a school using Class and Objects. 

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, height):
        try:
            height = int(height)
            if height <= 0:
                raise ValueError("Height must be a positive integer.")
            self.students.append({"name": name, "height": height})
        except ValueError as e:
            print(f"Error adding student {name}: {e}")

    def print_student_heights(self):
        print("Student Heights:")
        for student in self.students:
            print(f"{student['name']}: {student['height']} cm")
school = School()
school.add_student("Alice", 160)
school.add_student("Bob", "170")  
school.add_student("Charlie", -155)  
school.add_student("David", "abc")  

school.print_student_heights()
#====================================OUTPUT================================
# Error adding student Charlie: Height must be a positive integer.
# Error adding student David: invalid literal for int() with base 10: 'abc'
# Student Heights:
# Alice: 160 cm
# Bob: 170 cm