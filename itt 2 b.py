from collections import namedtuple, defaultdict, Counter, deque, OrderedDict
Employee = namedtuple('Employee', ['emp_id', 'name', 'department', 'salary'])
employees_records = OrderedDict()
department_groups = defaultdict(list)
task_queue = deque() 
def add_employee(emp_id, name, department, salary):
    """Adds a new employee if the ID is unique."""
    if emp_id in employees_records:
        print(f"Error: Employee ID {emp_id} already exists.")
        return
    
    new_emp = Employee(emp_id, name, department, salary)
    employees_records[emp_id] = new_emp
    department_groups[department].append(new_emp)
    print(f"Employee {name} (ID: {emp_id}) added successfully.")

def assign_task(emp_id, task_description):
    """Assigns a task to an employee if the ID is valid."""
    if emp_id not in employees_records:
        print(f"Error: Employee ID {emp_id} not found. Task assignment failed.")
        return
    
    task_queue.append((emp_id, task_description))
    print(f"Task '{task_description}' assigned to {employees_records[emp_id].name}.")

def complete_task():
    """Removes and completes the oldest task in the queue."""
    if not task_queue:
        print("No tasks currently in the queue.")
        return
    
    emp_id, task = task_queue.popleft()
    emp_name = employees_records[emp_id].name
    print(f"Task '{task}' completed by {emp_name} (ID: {emp_id}).")

def display_by_department():
    """Displays lists of employee names grouped by their department."""
    print("\n--- Employees by Department ---")
    for dept, emps in department_groups.items():
        names = [e.name for e in emps]
        print(f"{dept}: {', '.join(names)}")

def show_task_queue():
    """Displays all pending tasks."""
    print("\n--- Current Task Queue ---")
    if not task_queue:
        print("Queue is empty.")
    for emp_id, task in task_queue:
        print(f"[{employees_records[emp_id].name}]: {task}")

def display_department_summary():
    """Displays the total count of employees in each department."""
    print("\n--- Department Summary ---")
    counts = Counter(emp.department for emp in employees_records.values())
    for dept, count in counts.items():
        print(f"{dept}: {count} employees")
if __name__ == "__main__":
    print("1. Adding Employees:")
    add_employee(101, "Alice", "Engineering", 90000)
    add_employee(102, "Bob", "HR", 60000)
    add_employee(103, "Charlie", "Engineering", 95000)
    add_employee(101, "Duplicate", "Sales", 50000)  # Invalid case

    print("\n2. Assigning Tasks:")
    assign_task(101, "Fix server bug")
    assign_task(102, "Conduct interview")
    assign_task(999, "Secret mission")  # Invalid case

    show_task_queue()

    print("\n3. Processing Tasks:")
    complete_task()
    show_task_queue()

    display_by_department()
    display_department_summary()
