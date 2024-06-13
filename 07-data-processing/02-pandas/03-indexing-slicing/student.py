import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['London', 'New York', 'Paris', 'Paris', 'Sydney'],
    'Salary': [60000, 75000, 80000, 70000, 65000]
}

employees = pd.DataFrame(data)
print()

print("Access the last 2 rows and the 'Name' and 'Salary' columns using both label-based and positional-based indexing.")
print(employees.loc[3:4, ['Name', 'Salary']])

print()

print("Extract the data for employees with indices 0 to 2 and all columns using integer-based indexing.")
print(employees.iloc[0:2 , 0:4])

print()

print("Filter the data to include only employees aged 30 or above.")
print(employees[employees['Age'] >= 30])