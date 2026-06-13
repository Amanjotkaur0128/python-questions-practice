# #Question 1
# WAP Ask user to input a number and then month name corresponding to that number

# num = int(input("enter a number(1-12)"))
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# if 1 <= number <= 12:
#     print(f"The month corresponding to {number} is {months[number - 1]}")
# else:
#     print("Invalid input. Please enter a number between 1 and 12.")

#Question 2
#WAP Ask user to input 2 number,
#tell the followings
#1. Both number are equal or not
#2. Which is Bigger in both
#3. Either First NUmber is smaller or equal to Second Number
#4. Print your first name 5 times is first number is
#   greather than second and print your surname 3 times if 1st no
#   is less than second

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# if a > b: 
#     print(f"the number {a} is bigger")
# elif a < b:
#     print(f"the number {b} is bigger")
# else:
#     print("both numbers are equal")
# for i in range(5):
#     print("Aman")
#     if a > b:
#         for i in range(3):
#             print("kaur")
#     else:
#         for i in range(3):
#             print("jot")



# #Question 3:
#     Using User input ask user to input 2 string and tell followings
#     1. using == tell both string equal or not
#     2. using is operator tell both equal or not

# string1 = input("enter first string: ")
# string2 = input("enter second string: ")
# if string1 == string2:
#     print("both strings are equal")
# else :
#     print("both strings are not equal")
# if string1 is string2:
#     print("both strings are equal using")
# else:    print("both strings are not equal")



#Question 4:
    # ask user to input 2 string and convert it into numbers and using is op
    # tell both are equal or not

# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# num1 = int(string1)
# num2 = int(string2)
# if num1 is num2:
#     print("Both numbers are equal.")
# else:
#     print("Both numbers are not equal.")



# 5.  Python program to calculate the sum of all numbers from 1 to a given number.

# num =int(input("enter the no to sum upto: "))
# for i in range(num):
#     num+=i
# print(f"the value is {num}")



# 6.  Ask user to input a number and tell all even number
#    upto that number
#  Eg:
#    input a num:29
#    Even are:
#    2,4,6,... 28

# num = int(input("enter the number: "))

# for i in range(1,num + 1):
#     if i % 2 == 0:
#         print(i, end =" ")



# Problem Statement:
# You are tasked with creating a simple railway ticket booking system for a fictional railway company called CodeRail. The system should ask users for their age, travel class, and whether they want a meal included. Based on this input, the system will calculate and display the total ticket price.
# Requirements:
# 1. Ask the user for their name and age.
# 2. Ask them to choose a class:
# ⿡ First Class – ₹1500
# ⿢ Second Class – ₹1000
# ⿣ Sleeper Class – ₹500
# 3. If the passenger is under 5 years old, the ticket is free.
# 4. If the passenger is a senior citizen (60+), apply a 20% discount.
# 5. Ask if they want to add a meal:
# Yes – ₹200 extra
# No – No extra charge
# 6. Finally, print the passenger details and the final ticket price.

# print("-----Welcome to CodeRail Ticket Booking System-----")
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# print("Select travel class:")
# print("1. First Class – ₹1500")
# print("2. Second Class – ₹1000")
# print("3. Sleeper Class – ₹500")
# class_choice = int(input("Enter the number corresponding to your class choice: ")) 
# if class_choice == 1:
#     ticket_price = 1500
# elif class_choice == 2:
#     ticket_price = 1000
# elif class_choice == 3:
#     ticket_price = 500
# else:
#     print("Invalid class choice. Defaulting to Sleeper Class.")
#     ticket_price = 500
# if age < 5:
#     ticket_price = 0    
# else:
#     ticket_price *= 0.8
# meal_choice = input("Do you want to add a meal? (yes/no): ").strip().lower()
# if meal_choice == "yes":
#     ticket_price += 200
# print("\n-----Ticket Details-----")
# print(f"Name: {name}")
# print(f"Age: {age}")
# if class_choice == 1:
#     print("Class: First Class")
# elif class_choice == 2:
#     print("Class: Second Class")
# else:
#     print("Class: Sleeper Class")
# if meal_choice == "yes":
#     print("Meal: Included")
# print(f"Total Ticket Price: ₹{ticket_price:.2f}")
# print("Enjoy your journey! 🎉")



# Burger King has launched a self-order kiosk where customers can place their orders using a Python-based system. Your task is to build a simple Burger King order system in Python. The system should:
# - Display a menu with 3 items and their prices.
# - Let the user choose what they want to order and how many.
# - Ask the user if they have a 
# coupon code.
# - If the user enters a valid coupon code, apply the discount.
# - Display the final bill with or without discount applied.
# 🧾MENU
#   Item Price (₹)
# 1. Whopper Burger ₹150
# 2. Crispy Veg ₹100                                   
# 3. Chicken Wings ₹120                                
#Code Discount
#KING50- 50% off
# BK20- 20% off total
# NOCOUPON- No discount
# Use if-else statements to check coupon codes.
# Calculate total price based on the quantity.
# Apply the discount accordingly.
# Print a at the end.

# print("Welcome to Burger King 🍔!")
# print("menu: ")
# print("1. Whopper Burger - ₹150")
# print("2. Crispy Veg - ₹100")
# print("3. Chicken Wings - ₹120")
# ordered_item = int(input("Enter the item number (1/2/3):"))
# price = 0
# if ordered_item == 1:
#    price = 150
# elif ordered_item == 2:
#     price = 100
# else :
#     price = 120
# quantity = int(input("Enter quantity: "))
# price *= quantity

# coupon = input("do you have coupon code(yes/no): ")
# if coupon == "yes":
#     coupon_code = input("Enter the coupon code:")
#     print("applying coupon...")
#     print(f"Orignal Price: ₹{price}")
#     if coupon_code == "KING50":
#       print("Discount Applied: 50%")
#       print("Final Price: ₹",int(price*0.5))
#     elif coupon_code == "BK20":
#       print("Discount Applied: 20%")
#       print("Final Price: ₹", int(price*0.8))   
#     else :
#       print("No Discount")
#       print("Final Price: ₹", price)
# else :
#     print("final price: ", price)

# print("Thanks for ordering at Burger King! 🍟")