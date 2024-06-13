import pandas as pd

data = data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Salary': [60000, 75000, 80000, 70000, 65000]
}

employees = pd.DataFrame(data)
print()

print("First 3 rows of the Dataframe:")
print(employees.head(3))

print()

print("Summary statistics for the 'Salary' column of the Dataframe:")
print(employees['Salary'].describe())

print()

print("Amount of employees in a department")
print(employees['Department'].value_counts())

print()

print("Average salary of employees:")
print(employees['Salary'].mean())

print()

print("Employees with the highest salary")
print(employees[employees['Salary'] == employees['Salary'].max()])

print()

print("Department with the lowest average salary:", employees.groupby('Department')['Salary'].mean().idxmin())

print()

print("Add a new column 'Salary Increase' to the Dataframe, where each employee's salary is increased by 10%:")
employees['Salary Increase'] = employees['Salary'] * 1.1
print(employees[['Salary', 'Salary Increase']])