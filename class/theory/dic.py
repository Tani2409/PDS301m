import os
import csv
print('current dic: ', os.getcwd())

#transfer dic
# os.chdir(r"C:\Users\ADMIN\Documents\GitHub\PDS301m\class")
# print('current dic: ', os.getcwd())

# file = open("Textfile.txt","w")
# file.write("hello\n")
# file.close()

# file = open("Textfile.txt", "r")
# print(file.read())

# file = open("Textfile.txt","a")
# file.write("\ntoi dep trai")
# file.close()
# file = open("Textfile.txt", "r")
# print(file.read())

# file = open("names.txt","w")
# file.write("Tanh,Tu,Huy,Tan,Han")
# file.close()

# file = open("names.txt", "r")
# print(file.read())

# file = open("names.txt", "r")
# names = file.read().split(",")
# file.close()

# selectedname = input("choose 1 name: ")
# if selectedname in names:
#     names.remove(selectedname)

# file = open("names2.txt","a")
# file.write(str(names))
# file.close()
# file = open("names2.txt", "r")
# print(file.read())
# file.close()

# while True:
#     print("========Menu======== \n" \
#           "1) Create new file \n" \
#           "2) Display the file \n" \
#           "3) Add new item to the file \n" \
#           "what do you choose: ")
#     choice = input()
#     if choice == " ":
#         print("wrong input")
#         break
#     if choice == "1":
#         file = open("Subject.txt" ,"w")
#         file.write (input("what is your school subject name? "))
#         file.close()
#     if choice == "2":
#         file = open("Subject.txt","r")
#         print(file.read())
#         file.close()
#     if choice == "3":
#         file = open("Subject.txt","a")
#         file.write(input("What do you want to input: \n"))
#         file.close()
#         file = open("Subject.txt", "r")
#         print(file.read())

# Data to write
books = [
    ["Book", "Author", "Year Released"],  # header row
    ["To Kill A Mockingbird", "Harper Lee", 1960],
    ["A Brief History of Time", "Stephen Hawking", 1988],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1922],
    ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", 1985],
    ["Pride and Prejudice", "Jane Austen", 1813]
]

# Create and write to CSV file
with open("Books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books)
print("Books.csv created successfully!")

# Display the contents of the CSV file
with open("Books.csv", "r") as file:
    print("\n".join([", ".join(row) for row in csv.reader(file)]))

# Append new records to the CSV file
for _ in range(int(input("How many records do you want to add? "))):
    with open("Books.csv", "a", newline="") as file:
        csv.writer(file).writerow(input("Enter record (comma-separated): ").split(","))
print("Records added successfully!")

# Search for books by a specific author
author = input("Enter author name to search: ").strip().lower()
with open("Books.csv", "r") as file:
    books_by_author = [row for row in csv.reader(file) if row and row[1].strip().lower() == author]
if books_by_author:
    print(f"Books by {author}:")
    print("\n".join([", ".join(book) for book in books_by_author]))
else:
    print(f"No books found by '{author}'.")
