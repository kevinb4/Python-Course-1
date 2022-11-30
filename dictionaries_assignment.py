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

    # this is not part of this week's assignment
    # if rate > 37.30:
    #     print("An employee has a salary over $37.30 and may be a budget concern.")

# underpaid is not in the instructions
# underpaid_employees = []

# for hourly_rate in total_hourly_rate:
#     if hourly_rate > 28.15 and hourly_rate < 30.65:
#         underpaid_employees.append(hourly_rate)

# 6. calculate a raise on original salary values based off of certain criteria
company_raises = []

for salary in employee_salaries:
    if salary >= 22 and salary <= 24:
        company_raises.append(salary * 0.05)
    elif salary > 24 and salary <= 26:
        company_raises.append(salary * 0.04)
    elif salary > 26 and salary <= 28:
        company_raises.append(salary * 0.03)
    else:
        company_raises.append(salary * 0.02)

database = [] # declare the new list

index = 0

# since all of the lists are the same length, we can use the index
for name in employee_names:
    database.append({ 'id': employee_ids[index], 'name': name, 'salary': employee_salaries[index], 'total_hourly_rate': total_hourly_rate[index] })

    index = index + 1 # increment the index so we don't get duplicate data

print(database)