##Amira Muhammad
🌟 Python Mini Projects Collection
This repository contains a collection of educational Python mini-projects created as part of the Python Programming Fundamentals course at ITI (Information Technology Institute), under the guidance of Eng. Omar Shaqra. Each project is designed to demonstrate essential programming concepts, modularity, and code reusability.

🔧 Features
1. Pyramid Pattern Generator
Prints right-aligned triangle and simple pyramid star patterns.

Organized using modular functions.

📁 Files: pyramids.py, main.py

2. Vowel Counter
Counts vowels in a string using a dedicated function.

📁 Files: vowel_counter.py, main.py

3. Find Index of 'i' or 'I'
Displays all positions of the letter 'i' or 'I' in a user-input string.

📁 Files: find_i_index.py, main.py

4. Multiplication Tables
Generates multiplication tables for any number.

📁 Files: multiplication_table.py, main.py

5. Sort List
Accepts 5 numbers, then sorts them in ascending and descending order.

📁 Files: list_sorter.py, main.py

6. Validate Email and Name
Validates names and email input (Simple and Full modes).

📁 Files: Email_user_input_module.py, main.py

7. User Login Validation
Verifies username and password, with error handling.

📁 Files: login_validation.py, main.py

🧩 OOP Project: Real-Life Simulation
As part of the OOP section of the course, we built a structured simulation involving real-world classes and behaviors:

✅ Project Requirements
Design a system using 4 main classes:

🔹 Person
Attributes: name, money, mood, healthRate

Methods: sleep(hours), eat(meals), buy(items)

🔹 Employee (inherits from Person)
Attributes: id, car, email, salary, distanceToWork

Methods: work(hours), drive(distance), refuel(gasAmount), send_mail(to, subject, body)

🔹 Car
Attributes: name, fuelRate, velocity

Methods: run(velocity, distance), stop()

Constraints: velocity ∈ [0, 200], fuelRate ∈ [0, 100]

🔹 Office
Attributes: name, employees (list)

Methods:

get_all_employees(), get_employee(empId), hire(employee), fire(empId)

deduct(empId, amount), reward(empId, amount), check_lateness(empId, moveHour)

calculate_lateness() (static method)

Class Variable: employeesNum

Class Method: change_emps_num(num)

🧪 Testing Scenario
A simple simulation:

Samy, an employee with a Fiat 128 car.

Works at ITI Smart Village.

Drives 20 km daily.

Must arrive before 9:00 AM, else marked as late.

Office applies reward or deduction based on arrival.

The car consumes 10% fuel for every 10 km.

▶️ How to Run
Run main.py.

Choose the desired module.

Enter your inputs.

View the results in the terminal.



## 🧩 Modular Design

Each feature is implemented as a separate module, making the code:

* Easy to read and maintain.
* Reusable for future expansion.
* Beginner-friendly and structured.

---


