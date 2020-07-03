Path = 'files/Dog'
try:
    with open(Path) as file_path:
        file = file_path.read()
    print(file)
except FileNotFoundError as error:
    print("file is not found",error.filename)
print("Done......")
Path1 = 'files/Cat'
try:
    with open(Path1) as file_path:
        file = file_path.read()
    print(file)
except FileNotFoundError as error:
    print("file is not found ",error.filename)
print("Done....")

