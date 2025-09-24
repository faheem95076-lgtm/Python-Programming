file = open("student.txt","a")
# write, writelines
file.write("Hello c++\n")
text = b"Hello Nandhan"

file.close()
file = open("students.txt","r")
content = file.read()
print(content)
file.close()

# types of read:
# 1.read()=>
# 2.readline()=>
file = open("students.txt","r")
content = file.read()
print(content)
file.close()
# # 2.readline() =>
file = open("students.txt","r")
content = file.readline() #1st line
content1 = file.readline() #2st line
content2 = file.readline() #3st line
print(content)
print(content1)
print(content2)
file.close()

# # 3.readlines =->
file = open("students.txt","w")
file.write("Hello c++\n")
file.write("Hello Python \n")
lines = ["Hello Faheem\n","Hello Varshith\n","Hello World\n","Hello Python\n"]
file.writelines(lines)
file.close()

file = open("students.txt","a")
file.write("Hello c++\n")
text = b"Hello Faheem"
file.close()
