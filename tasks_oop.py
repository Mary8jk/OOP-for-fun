class Task:

    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        k = 'Сделана' if self.status is True else 'Не сделана'
        print(f'{self.name} ({k})')


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:

    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, st_task):
        self.st_task = st_task
        self.st_task.status = True

    def mark_undone(self, unst_task):
        self.unst_task = unst_task
        self.unst_task.status = False

    def show_tasks(self):
        for i in self.task_list.tasks:
            i.display()


# Ниже код для проверки классов Task, TaskList и TaskManager
# Создаем список задач
todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)

# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()
