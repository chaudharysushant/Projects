while True:

    print("\nMenu:")
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

  
    if choice == '1':
        print("You selected Option A")
    elif choice == '2':
        print("You selected Option B")
    elif choice == '3':
        print("You selected Option C")
    elif choice == '4':
        print("Exiting the menu. Goodbye!")
        break
    else:
    
        print("Invalid choice, please try again.")
