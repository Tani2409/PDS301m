def menu():
    print("========Menu======== \n" \
      "1) Add name \n" \
      "2) Change name \n" \
      "3) Remove name \n" \
      "4) Display names \n" \
      "5) Exit \n" \
      "what do you choose: ")

    choice = input()
    return choice

def add_name():
    name = input("Enter the name to add: ")
    with open("names.txt", "a") as file:
        file.write(name + "\n")
    print(f"{name} has been added.")

def display_names():
    with open("names.txt", "r") as file:
        names = file.readlines()
    print("Names in the file:")
    for name in names:
        print(name.strip())    

def change_name():
    old_name = input("Enter the name to change: ")
    new_name = input("Enter the new name: ")
    with open("names.txt", "r") as file:
        names = file.readlines()
    with open("names.txt", "w") as file:
        for i in names:
            if i.strip() == old_name:
                file.write(new_name + "\n")
            else:
                file.write(i)
    print(f"{old_name} has been changed to {new_name}.")

def remove_name():
    remove_name = input("Enter the name to remove: ")
    with open("names.txt", "r") as file:
        names = file.readlines()
    with open("names.txt", "w") as file:
        if remove_name in names:
            names.remove(remove_name)
            file.writelines(names)
        else:
            print(f"{remove_name} not found.")
    print(f"{remove_name} has been removed.")

def main():
    while True:
        choice = menu()
        if choice == "1":
            add_name()
        elif choice == "2":
            change_name()
        elif choice == "3":
            remove_name()
        elif choice == "4":
            display_names()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()