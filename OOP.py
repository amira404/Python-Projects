

# ------------------ Person Class ------------------
class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10

# ------------------ Car Class ------------------
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if 0 <= velocity <= 200:
            self.velocity = velocity
        else:
            raise ValueError("Velocity must be between 0 and 200")

        fuel_consumed = (distance / 10) * 10
        self.fuelRate -= fuel_consumed
        if self.fuelRate <= 0:
            remain_distance = distance - ((self.fuelRate + fuel_consumed) / 10 * 10)
            self.fuelRate = 0
            self.stop(remain_distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Stopped before arriving. Remaining distance: {remain_distance} km.")
        else:
            print("Arrived at destination.")

# ------------------ Employee Class ------------------
class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self):
        velocity_used = self.car.velocity
        self.car.run(velocity_used, self.distanceToWork)
        return velocity_used

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)

    def send_mail(self, to, subject, body, receiver_name):
        print(f"Sending mail to {receiver_name} <{to}>")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        print("Email sent.")

# ------------------ Office Class ------------------
class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour, velocity):
        emp = self.get_employee(empId)
        if emp:
            is_late = self.calculate_lateness(9, moveHour, emp.distanceToWork, velocity)
            if is_late:
                self.deduct(empId, 10)
                print("Samy is late! Salary deducted.")
            else:
                self.reward(empId, 10)
                print("Samy is on time! Salary rewarded.")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            raise ValueError("Velocity cannot be zero while calculating lateness.")
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

# ------------------ Example Usage ------------------

# Create a car
samy_car = Car(name="Fiat128", fuelRate=100, velocity=60)

# Create an employee
samy = Employee(name="Samy", money=1000, mood="neutral", healthRate=100,
                emp_id=1, car=samy_car, email="samy@iti.gov", salary=5000, distanceToWork=20)

# Create an office
iti_office = Office(name="ITI Smart Village")
iti_office.hire(samy)

# Simulate Samy's day
samy.sleep(7)
samy.eat(3)
samy.buy(2)
samy.work(8)
velocity_used = samy.drive()  # Save the velocity before car stops
iti_office.check_lateness(samy.id, moveHour=7.5, velocity=velocity_used)

# Final Output
print("--- Samy Info ---")
print(f"Name: {samy.name}")
print(f"Mood: {samy.mood}")
print(f"Health: {samy.healthRate}%")
print(f"Money: {samy.money} L.E")
print(f"Salary: {samy.salary} L.E")
print(f"Fuel: {samy.car.fuelRate}%")
