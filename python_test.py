# Given a list of numbers, print the sum of numbers present at even index positions.


# number = [10, 20, 30, 40, 50, 60]
# sum_even_index = sum(number[i] for i in range(len(number)) if i % 2 == 0)
# print("sum of numbers present at even index positions:", sum_even_index)



# Write a program to count how many times each character appears in a given string.


# string = "hello world"
# char_count = {}
# for char in string:
#     char_count[char] = char_count.get(char, 0) + 1
# print("Character counts:", char_count)



# Write a function that takes a string and returns:
# • number of uppercase letters
# • number of lowercase letters


# def count_case(string):
#     uppercase_count = sum(1 for char in string if char.isupper())
#     lowercase_count = sum(1 for char in string if char.islower())
#     return uppercase_count, lowercase_count
# string = "Hello World"
# print("uppercase letters:", count_case(string)[0])
# print("lowercase letters:", count_case(string)[1])



# Given two lists:
# subjects = ["Math", "Physics", "Chemistry"]
# marks = [85, 78, 92]
# Use zip() to create a dictionary and print the subject with the highest marks.


# subjects = ["Math", "Physics", "Chemistry"]
# marks = [85, 78, 92]
# subject_marks = dict(zip(subjects, marks))
# print("subject with the highest marks:", max(subject_marks, key=subject_marks.get))



# Using enumerate(), print the index of all negative numbers in a list.


# list = [10, -5, 20, -15, 30, -25]
# for index, value in enumerate(list):
#     if value < 0:
#         print(f"Index of negative number {value} is {index}")



# Write a program to check whether two lists contain the same elements (order does not matter).


# list1 = [1, 2, 3, 4]
# list2 = [5, 4, 3, 2, 1]
# if sorted(list1) == sorted(list2):
#     print("the two list contain the same elements.")
# else:
#     print("the two list do not contain the same elements.")
 


# Write a program to print the pattern:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5


# for i in range(5, 0, -1):
#     for j in range(5, 5-i, -1):
#         print(j, end = " ")
#     print()



# Write a program that removes duplicate elements from a list and keeps only unique elements.


# list_with_duplicates = [1, 2, 3, 2, 4, 1, 5]
# print("original list:", list_with_duplicates)
# unique_list = list(set(list_with_duplicates)) 
# print("list with unique elements:", unique_list)



# Given:
# names = ["A", "B", "C", "D"]
# scores = [45, 78, 90, 60]
# Using zip() and enumerate(), print:
# 1 - A scored 45
# 2 - B scored 78
# 3 - C scored 90
# 4 - D scored 60


# names = ["A", "B", "C", "D"]
# scores = [45, 78, 90, 60]
# dict_scores = dict(zip(names, scores))
# for i, j in enumerate(dict_scores):
#     print(f"{i+1} - {j} scored {dict_scores[j]}")



# Write a function that checks whether a list is increasing order or not.
# Return True if increasing, otherwise False.


# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
# def is_increasing(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] >= lst[i + 1]:
#             return False
#         else:
#             return True
# print(is_increasing(list1))
# print(is_increasing(list2))



# Write a program that:
# • Takes a sentence from the user
# • Prints the number of characters (excluding spaces)
# • Prints the sentence in uppercase
# • Prints the sentence reversed


# sentence = input("Enter a sentence:")
# print("Number of characters (excluding spaces):", len(sentence.replace(" ", "")))
# print("Sentence in uppercase: ", sentence.upper())
# print("Sentence reversed: ", sentence[::-1])



# Write a program that keeps asking the user to enter a number.
# Stop the loop when the user enters 0, then print the total sum of all entered numbers.


total_sum = 0
# while True:
#     number = int(input("Enter a number (0 to stop): "))
#     total_sum += number
#     if number == 0:
#         print("total sum of all entered number is:", total_sum)
#         break