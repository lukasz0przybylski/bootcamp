class Employee:
    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.register_time = 0

    def register_time(self, hours):
        self.register_time = hours

    def pay_solary(self):
        return self.rate_per_hour * self.register_time


def test_employee_initialization():
    employee = Employee("Jan", "Kowalski", 100)

    assert employee.name == "Jan"
    assert employee.last_name == "Kowalski"
    assert employee.rate_per_hour == 100


def test_pay_solary():
    employee
