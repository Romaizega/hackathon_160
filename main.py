from db import add_task, get_all_tasks, delete_task, mark_done, get_task_description
from weather import get_weather


def get_user_menu_choise():

    print ("""====== TODO LIST ======
        1. Show the weather
        2. Add a task
        3. Show all tasks
        4. Mark the task as done
        5. Delete the task
        6. Exit
    """)
    while True:
        try:
            user_input = int(input("Please eneter your choice: "))
            if user_input not in range(1, 7):
                print("⚠️ Wrong number, try again")
                continue
        except ValueError:
            print("⚠️ Please enter a number only")
            continue
        if user_input == 1:
            get_weather()

        if user_input == 2:
            new_task = input("Write your new task: ").strip()
            if new_task:
                add_task(new_task)
                print(f"Your  task: {new_task} added")
                get_all_tasks()
            else:
                print("Task cannot be empty!")
        elif user_input == 3:
            get_all_tasks()
        
        elif user_input == 4:
            try:
                task_id = int(input("Enter task id for mark: "))
                task_desc = get_task_description(task_id)
                mark_done(task_id)
                print(f"Your {task_desc} marked as ✅")
                get_all_tasks()
            except ValueError:
                print("Please enter a valid task ID")
                
        elif user_input == 5:
            try:
                delete_id = int(input("Write task id for delete task: "))
                task_desc = get_task_description(delete_id)
                delete_task(delete_id)
                print(f"Your {task_desc}  deleted ❌")
                get_all_tasks()
            except ValueError:
                print("Please enter a valid task ID")
        elif user_input == 6:

            print("Goodbye")
            break
        
get_user_menu_choise()
