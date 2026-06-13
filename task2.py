# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return ‘not a valid string’ instead of the empty string
# Sample string: - “Coder roots”
# Expected result - “cots”
# Sample string - “New year”
# Expected result - “near”

# string1 = input("enter the string: ")
# str2 = string1[0:2] + string1 [-2:]
# print(str2)


# Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string
# Sample String : 'coder', 'roots'
# Expected Result : 'roder coots'

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# new_str1 = str2[0] + str1[1:]
# new_str2 = str1[0] + str2[1:]
# result = new_str1 + " " + new_str2
# print("Result:", result)



# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# string = input("Enter a string: ")
# if len(string) < 3:
#     print(string)
# elif string.endswith("ing"):
#     print(string + "ly")
# else:
#     print(string + "ing")



# Write a Python program to remove the nth index character from a nonempty string

# string = input("Enter a string: ")
# remove = int(input("Enter the index you want to remove: "))
# str2 = string[ : remove] + string[remove+1:]
# print(str2)



# 1.   Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend
# at user choice
# Ex: [1,2,3,4,5]
# -> Enter anothe fiend: Raju
# [1,2,3,4,5,"Raju"]
# --> Most import afiedn: Billa
# --> Please location for billa: 1
# [1,"Billa",3,4,5,"Raju"]

# li = [1,2,3,4,5]
# print(li)
# another_friend = input("enter another friend: ")
# li.append(another_friend)
# print(li)
# imp_friend = input("Most important friend: ")
# index = input(f"please enter the location for {imp_friend}: ")
# li.insert(index,imp_friend)
# print(li)



# 2. Create a list of 10 number and print the list

# li = [1,2,3,4,5,6,7,8,9,10]
# print(li)



# 3.  Create a list [1,10,100,3,6,8] and add 59 on 3 location after
# that append 5 and print list and length of list

# numbers = [1, 10, 100, 3, 6, 8]
# numbers.insert(3, 59)
# numbers.append(5)
# print(numbers)
# print("Length of list:", len(numbers))



# Find all of the words in a list of strings that are less than 4 letters

# words = ["cat", "apple", "dog", "sun", "house", "pen"]
# for word in words:
#     if len(word) < 4:
#         print(word)



# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

# li = ["even" if i % 2 == 0 else "odd" for i in range(20)]
# print(li)



# Find all of the numbers from 1-1000 that are divisible by 7 

# li = [i for i in range(1,1001) if i % 7 == 0]
# print(li)



# Count the number of spaces in a string

# string ="hlo my name is Amanjot kaur"
# print(string.count(" "))



# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# new = [i for i in list_a for j in list_b if i==j]
# print(new)
