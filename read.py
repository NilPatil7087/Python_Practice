file_path = 'learning_python.txt'
with open('learning_python.txt') as file:
    summary = file.read()
print("______Python summary_________\n", summary)
print("--"*40)
#Read a file line by line
print("read a file line by line\n")
with open(file_path) as file:
    for line in file:
        print(line.strip())
print("--"*40)
#create a list of file
with open(file_path) as file:
    lines = file.readlines()
no_of_lines = len(lines)
print("no_of_lines",no_of_lines)

for i in range(no_of_lines):
    print(lines[i].rstrip())


