from User import User
class Admin(User):
    def __init__(self,First_name, Last_name,age, contact_no, login_attempt):
        super().__init__(First_name, Last_name,age, contact_no, login_attempt)
        self.privileges = ["can add post","can delete post","can modify post","can ban user"]

    def display_privilege(self):
        print("\n Admin's privileges")
        for list in self.privileges:
            print("\t",list)




admin = Admin("Nilesh","Patil","25","8390389256",4)
admin.greet_employee()
admin.Employee_info()
admin.login_attempt()
admin.display_privilege()



