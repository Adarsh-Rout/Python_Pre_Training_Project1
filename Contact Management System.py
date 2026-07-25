import json

def add_person():
    Name = input("Enter your name: ")
    Age = input("Enter your age: ")
    Email = input("Enter your email: ")

    person = {
        "Name": Name,
        "Age": Age,
        "Email": Email
    }
    return person

def display_people(people):
    for i, person in enumerate(people):
            print(i+1, "-", person["Name"],"|", person["Age"], "|", person["Email"])

def delete_person(people):
    display_people(people)

    while True:
        number = input("Enter the number of the person to delete: ")
        try:
            number = int(number)
            if 1 <= number <= len(people):
                people.pop(number - 1)
                return True
            else:
                print("Invalid number. Please try again.")
                return False
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        return False

def search_person(people):
    search_name = input("Enter the name of the person to search for: ").lower()
    
    result = []

    for person in people:
        name = person["Name"].lower()
        if search_name in name:
            result.append(person)
    display_people(result)

print("Welcome to the Contact Management System")
print()

with open("contacts.json", "r") as file:
    people = json.load(file)["contacts"]

people = []

while True:
    print("Current contacts:", len(people))
    if not people:
        print("No contacts available.")

    print("Please choose an option:")
    print("1. Add a person")
    print("2. Delete a person")
    print("3. Search for a person")
    print("4. Exit")
    command = input("Enter your choice (1, 2, 3, or 4): ")

    if command == "1":
        person = add_person()
        people.append(person)
        print()
        print("Person added successfully.")
        print()

    elif command == "2":
        if delete_person(people):
            print()
            print("Person deleted successfully.")
            print()
        else:
            print("Person not found.")

    elif command == "3":
        search_person(people)

    elif command == "4":
        print("Exiting the Contact Management System.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

with open("contacts.json", "w") as file:
    json.dump({"contacts": people}, file, indent=4)