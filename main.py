#Менеджер задач

#Задача: Создай класс Task, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
#(выполнено/не выполнено). Реализуй функцию для добавления задач,
#отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    all_tasks = []

    def __init__(self, description, deadline ):

        self.description = description
        self.deadline = deadline
        self.status = False
        Task.all_tasks.append(self)

    def display_current_tasks():
        print("Список текущих (не выполненных) задач ")

        for task in Task.all_tasks:
            if task.status == False:
                print(f" Описание: {task.description}, срок выполнения {task.deadline}")

    def mark_as_done(self):
        self.status = True

task1 = Task("Подготовить презентацию ", " 10 апреля")
task2 = Task("Отправить отчет"," 15 апреля")
task3 = Task("Позвонить клиенту", " 8 апреля")

Task.display_current_tasks()

task2.mark_as_done()

Task.display_current_tasks()