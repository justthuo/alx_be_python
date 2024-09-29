# Initialize an empty shopping list
shopping_list = []

def display_menu():
    """
    Display the menu options to the user.
    """
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item():
    """
    Add an item to the shopping list.
    """
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"Added '{item}' to the list.")

def remove_item():
    """
    Remove an item from the shopping list.
    """
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list.")
    else:
        print(f"'{item}' not found in the list.")

def view_list():
    """
    Display the current shopping list.
    """
    print("Current Shopping List:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")

def main():
    """
    Main loop to manage the shopping list.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()