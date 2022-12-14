# if elifs
age = 120

if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    "You're too young to party"

# Output: You are too old to party, granny.

# Simulating switch / case
# Old < 3.10
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))  

"""
Output: 
You can become a web developer.
You can become a backend developer.
You can become a mobile app developer
"""

# Pattern Matching >= 3.10
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
