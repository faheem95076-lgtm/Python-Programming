# 1. zero division error
try:
    a = int(input("Entre the numerator: "))
    b = int(input("Entre the Dinominartor: "))
    c = a%b
    print(c)
except ZeroDivisionError:
    print("Error:Division by zero is not possible")

try:
    i = 3
    n = int(input("Entre the n value: "))
    if i%n==0:
        print("Yes,number is multiple of",n)
    else:
        print("No ,number not is multiple of",n)

except ZeroDivisionError:
    print("Error: Divison by zero is not possible ")

# value error :
try:
    rollno = int(input("Entre your rollno: "))
except ValueError:
    print("Error: Given value is not in the integer dataypye. ")

#IndexError: 
try:
    list1 = [10,20,30]
    n = int(input("Entre the index value: "))
    print(list1[n])
except IndexError:
    print("Error:Given index value is not found in list1. ")

# Keyerror:
try:
    BioData  = {"Name":"Faheem","Rollno":"J9","Place":"Maismmaguda" }
    print(BioData["Branch"])
except KeyError:
    print("Given key value is not present in BioData")

# TypeError:
try:
    List = [10,20,30]
    sum = List + 5
    print(sum)
except TypeError:
    print("Invalid type operation")

# NameError:
try:
    print(Mult)
except NameError:
    print("Varible is not declared ")

# filenotfounderror:
try:
    file = open("details .txt","r")
    print(file.read())
except:
    print("File is not found in the system.")
finally:
    print("program is excuted")
