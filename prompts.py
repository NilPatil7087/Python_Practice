file = 'guest.txt'
print(f"creating file  {file}.....")
with open(file, 'w') as file_object:
    file_object.write("I Like to Play Games.\n")
    file_object.write("python is very dynamic and ")
    file_object.write("flexible.")
print(f"file {file} created \n")

while True:
    name = input("Enter your Name : ")
    user = input("which programming language do you like ? :")
    if name == 'quit':
        break
    else:
        with open(file, 'a') as file_object:
            file_object.write(name + "\n")
            file_object.write(user + "\n")
        print(f"Hii {name}\n welcome")
