to_do_list = []
print("******************Welcome to to-do list******************")
print("""\t Select an option
      \t 1. Add a task
      \t 2. View a task
      \t 3. Delete a task
      \t 4. Exit """)
while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter a task: ")
        to_do_list.append(task)
        print("Task added successfully!")
    elif choice == 2:
        if len(to_do_list) == 0:
            print("Enter your task in to-do list first")
        else:
            print("Tasks:")
            for task in to_do_list:
                print(task)
    elif choice == 3:
        if not to_do_list:
            print("Enter your task in to-do list first")
        else:
            to_do_list.pop()
            print("Task deleted successfully")
            
    elif choice == 4:
        print("Thank you for using to-do-list, have a nice day!")
        break
    else:
        print("Invalid choice")
print("Program terminated")
