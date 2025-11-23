# Simple use of IMPORTING DEF by De Mesa, Adrian ^^

from activity24_1 import info, cont

cont(input("Are you okay? (y/n): "))

if cont == 'y':
    print("I'm Glad!")
elif cont == 'n':
    print("Well uhh I hope you'll be okay I guess...")

print("\n So uhh at least provide some basic info about urself ;D\n")
name = input("Name: ")
loc = input("Location: ")
age = input("Age: ")

info(name, loc, age)
