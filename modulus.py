#The modulus operator, represented by the symbol %, is used in Python to return the remainder of a division operation. Here are a few examples to illustrate its use:

#Basic Modulus Operation
print(10 % 3)  # Output: 1
#In this example, when 10 is divided by 3, the quotient is 3 and the remainder is 1. The modulus operator returns this remainder, which is 1.

#Modulus with Zero
print(10 % 0)  # Output: Error
#In this case, Python will throw a ZeroDivisionError because you cannot divide by zero.

#Modulus with a Larger Number
print(3 % 10)  # Output: 3
#When the second number (divisor) is larger than the first number (dividend), the modulus operation will return the dividend itself, which is 3 in this case.

#Modulus with Negative Numbers
print(-10 % 3)  # Output: 2
#In Python, the modulus of a negative number is always positive. Here, -10 divided by 3 gives a quotient of -4 and a remainder of -1. But since Python always returns a positive remainder, it adjusts the quotient to -3 and the remainder to 2.

#Modulus for Checking Even or Odd Numbers
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")  # Output: Odd
#In this example, the modulus operator is used to check if a number is even or odd. If a number modulo 2 equals 0, it's an even number. Otherwise, it's an odd number. Here, 7 is an odd number, so "Odd" is printed.
