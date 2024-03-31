class Task:
    def __init__(self, description, start_date, due_date, priority):
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.priority = priority
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"{self.description} (с {self.start_date} до {self.due_date}, приоритет: {self.priority}) - {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_task_from_input(self):
        description = input("Описание задачи: ")
        start_date = input("Дата начала (число, месяц): ")
        due_date = input("Срок выполнения, к какой дате (число, месяц): ")
        priority = input("Приоритет (низкий, средний, высокий): ")
        new_task = Task(description, start_date, due_date, priority)
        self.add_task(new_task)
        print("Задача добавлена.")

if __name__ == "__main__":
        manager = TaskManager()
        while True:
            action = input(
                "Введите 'добавить задачу' для добавления задачи, 'показать задачи' для показа текущих задач, 'отметить выполненным' для отметки выполненной задачи, 'выйти' для выхода: ")
            if action == "добавить задачу":
                manager.add_task_from_input()
            elif action == "показать задачи":
                manager.show_current_tasks()
            elif action == "отметить выполненным":
                description = input("Описание выполненной задачи: ")
                manager.mark_task_done(description)
            elif action == "выйти":
                print("Выход из программы.")
                break
            else:
                print("Неизвестная команда.")

