# class Vehicle:
#     color = "white"

#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = None

#     def assign_seating_capacity(self, seating_capacity):
#         self.seating_capacity = seating_capacity

#     def display_properties(self):
#         print("Properties of the Vehicle:")
#         print("Color:", self.color)
#         print("Maximum Speed:", self.max_speed)
#         print("Mileage:", self.mileage)
#         print("Seating Capacity:", self.seating_capacity)


# # Creating objects of the Vehicle class
# vehicle1 = Vehicle(200, 20)
# vehicle1.assign_seating_capacity(5)
# vehicle1.display_properties()

# vehicle2 = Vehicle(180, 25)
# vehicle2.assign_seating_capacity(4)
# vehicle2.display_properties()


class Student:
    school_name = "FPT University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("School Name:", Student.school_name)

    def change_name(self):
        new_name = input("Enter new name: ")
        self.name = new_name
        print("Name changed successfully!")

    # class method
    @classmethod
    def change_school_name(cls, new_school_name):
        cls.school_name = new_school_name
        print("School name changed successfully!")


# --- Tạo và chạy đối tượng ---
s1 = Student("Tanh", 21)
s1.display_student_info()

s1.change_name()
Student.change_school_name("Hutech")

s1.display_student_info()
