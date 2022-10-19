from .location_requests import get_single_location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Kiya",
    },
    {
        "id": 2,
        "name": "Qira",
    },
    {
        "id": 3,
        "name": "Lyra",
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    
    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    single_location = get_single_location(1)
    location_id = single_location
    employee["locationId"] = location_id["id"]
    EMPLOYEES.append(employee)
    return employee

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
