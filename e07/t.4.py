class Task:
    id_counter = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} - {status}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        new_task = Task(description, programmer, workload)
        self.orders.append(new_task)
        print("added!")

    def all_orders(self):
        return self.orders

    def finished_orders(self):
        return [task for task in self.orders if task.finished]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.finished]

    def mark_finished(self, task_id):
        for task in self.orders:
            if task.id == task_id:
                task.mark_finished()
                print(f"command: 4id: {task_id} marked as finished")
                return
        print("erroneous input")

    def programmers(self):
        return list(set(order.programmer for order in self.orders))

    def status_of_programmer(self, programmer):
        finished = unfinished = 0
        finished_workload = unfinished_workload = 0
        for task in self.orders:
            if task.programmer == programmer:
                if task.finished:
                    finished += 1
                    finished_workload += task.workload
                else:
                    unfinished += 1
                    unfinished_workload += task.workload
        print(f"programmer: {programmer} tasks: finished {finished} not finished {unfinished}, hours: done {finished_workload} scheduled {unfinished_workload}")


def interactive_app():
    orders = OrderBook()

    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")

    while True:
        command = input("command: ").strip()

        if command == "0":
            break
        elif command == "1":
            try:
                description = input("description: ").strip()
                programmer_workload = input("programmer and workload estimate: ").strip().split()
                if len(programmer_workload) != 2:
                    raise ValueError("erroneous input")
                programmer = programmer_workload[0]
                workload = int(programmer_workload[1])
                orders.add_order(description, programmer, workload)
            except ValueError:
                print("erroneous input")
        elif command == "2":
            finished_tasks = orders.finished_orders()
            if finished_tasks:
                for task in finished_tasks:
                    print(task)
            else:
                print("no finished tasks")
        elif command == "3":
            unfinished_tasks = orders.unfinished_orders()
            if unfinished_tasks:
                for task in unfinished_tasks:
                    print(task)
            else:
                print("no unfinished tasks")
        elif command == "4":
            try:
                task_id = int(input("id: ").strip())
                orders.mark_finished(task_id)
            except ValueError:
                print("erroneous input")
        elif command == "5":
            programmers = orders.programmers()
            print("Programmers:", " ".join(programmers))
        elif command == "6":
            programmer = input("programmer: ").strip()
            if programmer not in orders.programmers():
                print("erroneous input")
            else:
                orders.status_of_programmer(programmer)
        else:
            print("erroneous input")

interactive_app()
