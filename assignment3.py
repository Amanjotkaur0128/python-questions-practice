# Write a program to find the sum of first n natural numbers(n is integer input from user)
# num = int(input("enter the number: "))

# for i in range(1,num):
#     num+=i
# print(f"the sum of natural number is {num}")



# Print the multiplication table of a given number using a for loop
# output - 2*2=4

# a = int(input("enter the number: "))
# b = int(input("upto: "))
# for i in range(1,b+1):
#     print(f"{a}x{i}={a*i}")



# write a program to check whether a given number is prime or not.
# n= int(input("Enter number "))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("number is not prime")
#             break
#     else:
#         print("prime")



# Check whether a number is a palindrome.
# num = int(input("enter the number: "))
# temp = num    
# rev = 0
# while temp > 0:
#     rev = rev * 10 + temp % 10
#     temp //= 10
# if num == rev:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")



#Print numbers from 1 to 100:
    # If divisible by 3 → print Fizz
    # If divisible by 5 → print Buzz
    # If divisible by both → print FizzBuzz

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz", i)
#     elif i%3==0:
#         print("Fizz", i)
#     elif i%5==0:
#         print("Buzz", i)
#     else:
#         print(i)



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

print("Thanks for ordering at Burger King! 🍟")