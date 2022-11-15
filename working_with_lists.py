# 1. list all walsh courses in lower case
courses = ["com-320", "com-340", "it-403", "it-405", "it-407", "it-410"]

# 2. sort list and loop through each one in uppercase letters
courses.sort()

for course in courses:
    print(f"I have taken {course.upper()} at Walsh College.")

# 3. add courses I plan to take next term and resort, plus print a message to note these are upcomming
courses.append("it-408")
courses.append("it-412")
courses.append("it-430")
courses.sort()

print("This is my course of study with upcoming courses added:")

for course in courses:
    print(course)

# 4. remove courses I've taken already (including in progress) and print each course removed along with printing a message
print("I do not have to take these courses:")
print(courses.pop(0)) # COM-320
print(courses.pop(0)) # COM-340
print(courses.pop(0)) # IT-403
print(courses.pop(0)) # IT-405
print(courses.pop(0)) # IT-407
print(courses.pop(1)) # IT-410

# 5. print out each item in the list of course left on its own line
print("I plan to take the following courses next term")

for course in courses:
    print(course)

# 6. create a list of numbers 1-1000 that are divisible by 6
numbers = list(range(6, 1_001, 6))

# 7. print out first 20 numbers in the list on their own line
print("Here are twenty numbers divisible by 6.")

for number in numbers[0:20]:
    print(number)

# 8. store maximum value of the previous list created as a variable (using python? what else would we use? or do you mean programmatically?)
maximum = max(numbers)

# 9. Print out the max number variable in the list with a message
print(f"The maximum value in the list is: {maximum}")

# 10. calcualte sum of values 10-50 and store it as a variable then print it
sum_of_values = sum(numbers[9:49]) # since lists are 0 indexed, we need to start at 9 to get the 10th value

print(f"Here is the sum of several values in the list: {sum_of_values}")

# 11. overwrite the courses variable with the original numbers list in #6
courses = numbers