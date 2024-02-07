from pact import Consumer, Provider
import requests
import atexit

# Define the employee schema
employee_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "department": {"type": "string"}
    },
    "required": ["name", "age", "department"]
}

# Create the Pact object
pact = Consumer('Dashboard').has_pact_with(Provider('Employee'), port=1234)
@pact.start_service()
@atexit.register
def at_exit():
  pact.stop_service()
# Define the interaction for getting all employees
@pact.given('A list of employees exists')
def test_get_all_employees():
    pact.will_respond_with(200, headers={"Content-Type": "application/json"}, body={"employees": [employee_schema]})
    result = requests.get('http://localhost:1234/employees')
    assert result.status_code == 200

# Define the interaction for getting an employee by ID
@pact.given('A specific employee exists')
@pact.upon_receiving('a request for employee by ID')
def test_get_employee_by_id():
    pact.will_respond_with(200, headers={"Content-Type": "application/json"}, body=employee_schema)
    result = requests.get('http://localhost:1234/employees/1')
    assert result.status_code == 200

# Run the tests
for interaction in pact.interactions:
    interaction.test_func()

# Verify the pact
pact.verify()
