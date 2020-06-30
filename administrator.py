from User import User


class Admin(User):
    def __init__(self, First_name, Last_name, age, contact_no, login_attempt):
        super().__init__(First_name, Last_name, age, contact_no, login_attempt)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges_list = ["can add post", "can delete post", "can ban user", "can modify post"]

    def describe_privileges(self):
        print("\nAdministrator's set of privileges:")
        for list in self.privileges_list:
            print("\t", list)


admin2 = Admin("Nilesh", "Patil", "22", "8390389256", 2)
admin2.greet_employee()
admin2.Employee_info()
admin2.privileges.describe_privileges()
