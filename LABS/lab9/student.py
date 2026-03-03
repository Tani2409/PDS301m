# school.py

class Student:
    """Represents a student with a name, ID, and enrolled courses."""
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course_name):
        """Adds a course to the student's course list."""
        self.courses.append(course_name)
        print(f"Enrolled in {course_name}.")

    def display_info(self):
        """Prints the student's information."""
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Courses: {', '.join(self.courses)}")

# --- Using the class ---
# Create an object (instance) of the Student class
student1 = Student("Alice", "S12345")

# Use the object's methods
student1.enroll("Python Programming")
student1.enroll("Database Systems")
student1.display_info()
