ass TodoList:
    def __init__(self, title=None):
        self.title = title
        self.tasks = list()

    def add_task(self, item):
        self.tasks.append(item)
        return self.tasks

todo_list = TodoList()
todo_list = TodoList()
todo_list = TodoList()
todo_list.add_task('Купить лампочку')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Выкинуть лампочку')
print("\n".join(todo_list.tasks))
