from actions import add_task, show_tasks, delete_task, mark_done


def menuOptions():
    print(
        """      
        ========== MENU ==========
          1.Add Task 
          2.Show Tasks 
          3.Delete Tasks 
          4.Mark Task As Done 
          5.Exit
          """
    )


while True:
    menuOptions()
    try:
        op = int(input("Pls Select An Option : "))
    except ValueError:
        print("Invalid input input ")
        continue
    if op == 1:
        task = input("pls enter the task title :")
        add_task(task)
    elif op == 2:
        show_tasks()
    elif op == 3:
        id = int(input("pls enter the task id : "))
        delete_task(id)
    elif op == 4:
        id = int(input("pls enter the task id : "))
        mark_done(id)
    elif op == 5:
        print("Exiting form the programe..")
        break
    else:
        print("invalid option...")
