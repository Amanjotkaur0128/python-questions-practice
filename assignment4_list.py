# 1.Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend at user choice

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
# li=[1,2,3,4,5,6,7,8,9]
# print(li)



# 3.  Create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list
# li =[1,10,100,3,6,8]
# print(li) 
# li.insert(3,59)
# print(li)
# li.append(5)
# print(li)
# print(len(li))



# Find all of the words in a list of strings that are less than 4 letters

# li = ["apple", "car", "bus","truck","cycle"]
# less_then_4 =[x for x in li if len(x)<4]
# print(less_then_4)



# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

# li = ["even" if x % 2 == 0 else "odd" for x in range(20)]
# print(li)



# Find all of the numbers from 1-1000 that are divisible by 7 

# li = [x for x in range(1,1001) if x%7 == 0]
# print(li)



# Count the number of spaces in a string

# string = "my name is Amanjot kaur"
# print(string.count(" "))



# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
li = [i for i in list_a for j in list_b if i==j]
print(li)