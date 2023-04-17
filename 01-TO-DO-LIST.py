import sys
import sqllite3

#Dodawanie zadań
def add_task():
    task = input("Wpisz zadanie: ")
    if task == "0":
        print("Spróbuj ponownie :)")
        sys.exit(0)
    else:
        tasks.append(task)


#Pokaż zadania

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task+ " [" + str(task_index) + "]")
        task_index +=1


#Usuwanie zadań