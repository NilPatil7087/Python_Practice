class user:

    def __init__(self, First_name, Last_name, age, contact_no, login_attempt):
        self.First_name = First_name
        self.Last_name = Last_name
        self.age = age
        self.contact_no = contact_no
        self.login_attempt = login_attempt

    def greet_employee(self):
        print(f"\n Hiii,Welcome {self.First_name}")

    def Employee_info(self):
        print("---EMPLOYEE INFORMATION---")
        print(f"Employee First Name: {self.First_name}")
        print(f"Employee Last Name: {self.Last_name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Contact_no: {self.contact_no}")
        print(f"Employee Login Attempt: {self.login_attempt}")

    def increment_login_attempt(self):
        print(f"number of login attempts : {self.login_attempt}")
        self.login_attempt += 1

    def reset_login_attempt(self, reset):
        print(f"reset the previous login attempts : {reset}")


Employee = user("Nilesh", "Patil","22","8390389256",2)
Employee.greet_employee()
Employee.Employee_info()
Employee.increment_login_attempt()
Employee.increment_login_attempt()
Employee.reset_login_attempt(0)
print("__"*30)

Employee2 = user ("Mayur","Patil","20","8830405941",4)
Employee2.greet_employee()
Employee2.Employee_info()
Employee2.increment_login_attempt()
Employee2.increment_login_attempt()
Employee2.increment_login_attempt()
Employee2.increment_login_attempt()
Employee2.reset_login_attempt(0)