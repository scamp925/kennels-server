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
