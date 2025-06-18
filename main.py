from db import add_task, get_all_tasks, delete_task, mark_done, get_task_description, get_unmark_task, edit_task
from weather import get_weather
from money import get_money
from datetime import datetime



def print_menu():
    print ("""MENU
        1. Show the weather
        2. Show currency
        3. Show all tasks
        4. Add a task
        5. Mark the task as done
        6. Delete the task
        7. Edit task
        8. Exit
    """)

date_now = datetime.now()

def get_user_menu_choise():

    print(f"Today: {date_now.strftime("%Y-%m-%d %H:%M:%S")}\n")
    print ("""=========== TODO LIST ===========
        1. Show the weather 🌦️
        2. Show currency 💱
        3. Show all tasks 📋
        4. Add a task ➕
        5. Mark the task as done ✅
        6. Delete the task ❌
        7. Edit task ✏️
        8. Exit 🚪
    """)
    while True:
        try:
            user_input = int(input("Please eneter your choice: "))
            if user_input not in range(1, 9):
                print(" Wrong number, try again")
                continue
        except ValueError:
            print("Please enter a number only")
            print_menu()
            continue
        if user_input == 1:
            get_weather()
            print_menu()
        
        elif user_input == 2:
            get_money()
            print_menu()

        elif user_input == 3:
            get_all_tasks()
            print_menu()

        if user_input == 4:
            new_task = input("Write your new task: ").strip()
            if new_task:
                add_task(new_task)
                print(f"Your  task: {new_task} added")
                get_all_tasks()
                print_menu()
            else:
                print("Task cannot be empty!")
        
        elif user_input == 5:
            try:
                task_id = int(input("Enter task id for mark: "))
                task_desc = get_task_description(task_id)
                mark_done(task_id)
                if task_desc:
                    print(f"Your {task_desc} marked as ✅")
                else:
                    print("Task not found")
                get_all_tasks()
                print_menu()
            except ValueError:
                print("Please enter a valid task ID")
                
        elif user_input == 6:
            try:
                delete_id = int(input("Write task id for delete task: "))
                task_desc = get_task_description(delete_id)
                delete_task(delete_id)
                if task_desc:
                    print(f"Your {task_desc}  deleted ❌")
                else:
                    print("Task not found")
                get_all_tasks()
                print_menu()
            except ValueError:
                print("Please enter a valid task ID")

        elif user_input == 7:
            try:
                edit_id = int(input("Write task id to edit the task: "))
                current_desc = get_task_description(edit_id)
                if not current_desc:
                    print("The task not found")
                else:
                    print(f"Current task: {current_desc}")
                    new_text = input("Edit your new task: ").strip()
                    if new_text:
                        edit_task(edit_id, new_text)
                        print(f"Task ID {edit_id} updated to: {new_text}")
                        print()
                        print_menu()
                    else:
                        print("Task cannot be empty")
            except ValueError:
                print("Please eneter a valid task ID")

        elif user_input == 8:
            print("You have unfinished tasks:")
            unmark = get_unmark_task()
            if unmark:
                print(unmark)
            else:
                print("Well done! You did it")
            print("Goodbye")
            break
        
get_user_menu_choise()
