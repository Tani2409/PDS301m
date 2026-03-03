# 1. Define the lists of students
robotics_club = ["Alice", "Bob", "Charlie", "David"]
debate_club = ["Charlie", "Eve", "Frank", "Alice"]

# 2. Convert lists to sets
robotics_set = set(robotics_club)
debate_set = set(debate_club)
print(f"Robotics Club Members: {robotics_set}")
print(f"Debate Club Members: {debate_set}")

# 3. Perform analysis using set operations
all_students = robotics_set | debate_set
both_clubs = robotics_set & debate_set
robotics_only = robotics_set - debate_set

print("\n--- Club Enrollment Analysis ---")
print(f"All unique students: {all_students}")
print(f"Students in both clubs: {both_clubs}")
print(f"Students only in the Robotics Club: {robotics_only}")
