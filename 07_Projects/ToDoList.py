tasks = []   # list saving tasks

while True:
    try:
        user_choice = int(input(
            f"************\nMenu:\n1: Add New Task\n2: View Tasks\n3: Delete Task\n4: Exit\n*************\nYour Choice: "
        ))

        if 1 <= user_choice <= 4:  #add new task
            if user_choice == 1:   
                new_task = input("What task do you want to add? ")
                tasks.append(new_task)
                print(f"Task '{new_task}' has been added.")

            elif user_choice == 2:  #view tasks
                if tasks:
                    print("Your Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}: {task}")
                else:
                    print("There are no tasks.")

            elif user_choice == 3:  #delete task
                if tasks:
                    try:
                        task_index = int(input("Which task (number) do you want to delete? ")) - 1
                        if 0 <= task_index < len(tasks):
                            completed_task = tasks.pop(task_index)
                            print(f"Task '{completed_task}' has been deleted.")
                        else:
                            print("Invalid number. Please enter a valid number.")
                    except ValueError:
                        print("Please enter a number.")

                else:
                    print("There are no tasks to delete.")

            elif user_choice == 4:  #exit
                print("Program exited.")
                break

        else:
            print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
