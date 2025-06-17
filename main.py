from db import add_task, get_all_tasks, delete_task, mark_done


def get_user_menu_choise():

    print ("""====== TODO LIST ======
        1. Add a task
        2. Show all tasks
        3. Mark the task as done
        4. Delete the task
        5. Exit
    """)
    while True:
        try:
            user_input = int(input("Please eneter your choice: "))
            if user_input not in range(1, 6):
                print("Wrong number, try again")
                continue
        except:
            print("Write onle a number")
            
        if user_input == 1:
            new_task = input("Write your new task: ")
            add_task(new_task)
        elif user_input == 2:
            get_all_tasks()
        elif user_input == 3:
            task_id = int(input("Enter task id for mark: "))
            mark_done(task_id)
        elif user_input == 4:
            delete_id = int(input("Write task id for delete task: "))
            delete_task(delete_id)
        elif user_input == 5:
            print("Goodbye")
            break
        
get_user_menu_choise()
