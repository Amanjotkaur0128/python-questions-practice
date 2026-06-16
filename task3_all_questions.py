#1. Write a program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# for i in range(1,50+1):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz",end=" ")
#     elif i%3 ==0:
#         print("Fizz",end=" ")
#     elif i%5==0:
#         print("Buzz",end=" ")
#     else:
#         print(i,end=" ")



# Write a program to print all prime numbers between 1 and 100

# for i in range(1, 101):
#     count = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1

#     if count == 2:
#           print(i,end=" ")



#  Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

# score = int(input("Enter your score (0-100): "))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# elif score >= 0:
#     print("Grade: F")
# else:
#     print("Invalid score")



# 4. Write a program that prints the multiplication table (from 1 to 10) for a given number

# num = int(input("enter the no: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {i*num}")



# 5. Write a program to create a list of the squares of the even numbers from 1 to 20.

# squares = [i**2 for i in range(1, 21) if i % 2 == 0]
# print(squares)



# 6. Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



# 7. Write a program that takes the lengths of three sides of a triangle as input and determines the type of triangle (equilateral, isosceles,  scalene or right angle tringle ).

# a = int(input("Side 1: "))
# b = int(input("Side 2: "))
# c = int(input("Side 3: "))

# if a == b == c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
#     print("Right Angle Triangle")
# else:
#     print("Scalene")



# 8. Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.

# num = int(input("Enter number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# 10. Write a program that calculates the Body Mass Index (BMI) and categorizes it based on the following criteria:
# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obesity

# weight = float(input("Weight (kg): "))
# height = float(input("Height (m): "))
# bmi = weight / (height ** 2)
# print("BMI =", bmi)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal Weight")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obesity")

# 11. Write a program that takes an integer input representing a day of the week (1 for Monday, 2 for Tuesday, etc.) and prints the corresponding day name.

# day = int(input("Enter day number: "))
# days = {
#     1:"Monday", 2:"Tuesday", 3:"Wednesday",
#     4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"
# }
# print(days.get(day, "Invalid Day"))



# 12. Write a program that calculates the discount on a product based on the following criteria:
# If the price is greater than $1000, a discount of 10% is applied.
# If the price is between $500 and $1000, a discount of 5% is applied.
# If the price is below $500, no discount is applied.

# price = float(input("Enter price: "))

# if price > 1000:
#     discount = price * 0.10
# elif price >= 500:
#     discount = price * 0.05
# else:
#     discount = 0

# print("Discount:", discount)
# print("Final Price:", price - discount)

# 13. Write a program to find the sum of the first n natural numbers.

# n = int(input("Enter n: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum =", total)

# 14. Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with name, department, and salary, filter and create a list of names of employees who have a salary greater than 50,000.

# employee_details = {
#     101: {"name":"Aman", "department":"IT", "salary":60000},
#     102: {"name":"Ravi", "department":"HR", "salary":45000},
#     103: {"name":"Simran", "department":"IT", "salary":70000}
# }
# result = [emp["name"] for emp in employee_details.values()
#           if emp["salary"] > 50000]
# print(result)



# 15. Write a program to count the number of vowels in a given string

# text = input("Enter string: ")
# count = 0
# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1
# print("Vowels:", count)



# 16. Write a program to find the sum of the digits of a given number.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print("Sum of digits:", total)



# 17. Write a program to print a pattern of stars. For example, if n = 5, the pattern should be
# *
# **
# ***
# ****
# *****

# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     print("*" * i)

# 18. Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. The program should give hints if the guess is too high or too low.

# random = 67
# while True:
#     guess = int(input("Guess: "))

#     if guess > random:
#         print("Too High")
#     elif guess < random:
#         print("Too Low")
#     else:
#         print("Correct!")
#         break

# 19. Ask user to input a number and show all even number upto that number starting from number 1
# Ex: 15
# 2 4 6 8 10 12 14

# num = int(input("Enter number: "))
# for i in range(2, num + 1, 2):
#     print(i, end=" ")

# 20. WAP Create a list of 10 elements (Number elements) and perform the following
# a. Tell element 25 exist or not
# b. Total length of List
# c. total occurrence of 25 in the list
# d. traverse of Each element
# e. Show All Even number in list

# lst = [10, 25, 30, 25, 40, 50, 60, 70, 25, 80]
# print("25 exists:", 25 in lst)
# print("Length:", len(lst))
# print("Occurrences of 25:", lst.count(25))
# print("Traverse:")
# for i in lst:
#     print(i)
# print("Even Numbers:")
# for i in lst:
#     if i % 2 == 0:
#         print(i)

# 21. Ask User to input a String of min 10 words and max 19 words and perform the following:
# 1. Print full string and length of string
# 2. Tell String is palindrome or not mean
# 3. Tell middle word in the string.
# 4. Print Second last word in the String.

# text = input("Enter 10-19 words: ")
# words = text.split()
# print("String:", text)
# print("Length:", len(text))
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# print("Middle Word:", words[len(words)//2])
# print("Second Last Word:", words[-2])

# 22. Perform the following Task as per the output
# Welcome to Calci:
# 1. Power
# 2. Sum
# 3. Sub
# 4. Multiple

# print("Welcome to Calci")
# print("1. Power")
# print("2. Sum")
# print("3. Sub")
# print("4. Multiply")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     a = int(input("Base: "))
#     b = int(input("Power: "))
#     print(a ** b)

# elif choice == 2:
#     a = int(input("First Number: "))
#     b = int(input("Second Number: "))
#     print("Sum =", a + b)

# elif choice == 3:
#     a = int(input("First Number: "))
#     b = int(input("Second Number: "))
#     print("Difference =", a - b)

# elif choice == 4:
#     a = int(input("First Number: "))
#     b = int(input("Second Number: "))
#     print("Product =", a * b)

# else:
#     print("Invalid Choice")

# Enter your choice. --> 2
# Enter 1st Number for Sum: 100
# Enter 2nd number for SUm: 200
# Sum is 300



# 23. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# example:
# Input :
# X = ['abc', 'xyz', 'aba', '1221']
# Output :

# X = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for s in X:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1
# print(count)