file_path = 'learning_python.txt'
with open(file_path) as file:
    for line in file:
        print(line.replace('Python', 'C').rstrip())
