#!/usr/bin/python3

while True:
    a = input("Enter yes/no to continue: ")
    if a=="yes":
        print("yes process.......")
        break
    elif a=="no":
        print("no process.......")
        break
    else:
        print("Enter either yes/no: ")
        continue    