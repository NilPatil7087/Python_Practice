#constraints
print("\t PI :3.14 \n second line")
language = "Python "
print(language,"_____")
print(language.rstrip(),"-----")
print(language.lstrip(),"-----")


#dictionary is collection of key values pairs

student ={"mayur":"1","nilesh":"2"}
print(student)

print("__"*30)

alien={}
alien={"color":"green","points":100}

#keys are unique
print(alien.get("color"))

print(alien["color"])

#change the key values
alien["color"] = "red"
print(alien)

#modify the value
alien["red"]=500
print(alien)


#access the value
print(alien["red"])

#delete the value
del alien["red"]
print(alien)
