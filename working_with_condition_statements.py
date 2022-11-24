# 1. create a single list with data given
employee_info = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False, 
24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 
22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False, 22.65, 1152, "David Toma"]

# 2. sort the information into three lists containing emplyee ID's, employee names, and employee salary info
employee_ids = []
employee_names = []
employee_salaries = []

for info in employee_info:
    # 3. make sure no duplicate data is put in the new lists
    if info not in employee_ids and info not in employee_names and info not in employee_salaries:
        if type(info) == int:
            employee_ids.append(info)
        elif type(info) == str:
            employee_names.append(info)
        elif type(info) == float:
            employee_salaries.append(info)

# 4. calcualte each salary by 1.3 into a new list and check if it's over 37.30
total_hourly_rate = []

for salary in employee_salaries:
    rate = salary * 1.3
    total_hourly_rate.append(rate)

    if rate > 37.30:
        print("An employee has a salary over $37.30 and may be a budget concern.")

# 5. check if any employee's rate is between 28.15 and 30.65 and add them to a new list
underpaid_employees = []

for hourly_rate in total_hourly_rate:
    if hourly_rate > 28.15 and hourly_rate < 30.65:
        underpaid_employees.append(hourly_rate)

# 6. calculate a raise on original salary values based off of certain criteria
company_raises = []

# typically when you state something should be "in between a rage of two numbers",
# those exact numbers are not included because they are not "in between". (ref to previous assignment)
# however, when writing a function like this, it doesn't make sense to exclude
# salaries that are exactly $22 or $24. because if we pass $24.00, it will end up
# in the last else clause
for salary in employee_salaries:
    if salary >= 22 and salary <= 24:
        company_raises.append(salary * 0.05)
    elif salary > 24 and salary <= 26:
        company_raises.append(salary * 0.04)
    elif salary > 26 and salary <= 28:
        company_raises.append(salary * 0.03)
    else:
        company_raises.append(salary * 0.02)

# 7. write my own multiple elif condition with at least four different tests
ages = list(range(1,23))
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# this will loop through the age ranges of when a person may be in a specific grade/college level
# disclaimer: I'm not real knowlegable in age ranges so these may be inaccurate
for age in ages:
    if age < 7:
        print(f"At age {age}, a person will typically not be in school yet")
    elif age >= 7 and age <= 11:
        print(f"At age {age}, a person will typically be in grade school (grades 1-5)")
    elif age >= 12 and age <= 14:
        print(f"At age {age}, a person will typically be in middle school (grades 6-8)")
    elif age >= 15 and age <= 18:
        print(f"At age {age}, a person will typically be in high school (grades 9-12)")
    elif age > 18:
        print(f"At age {age}, a person will typically have graduated high school and might be in college")
    else: # not really needed in this case but it's good to have a safety net
        print(f"The age {age} is unaccounted for")