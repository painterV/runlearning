import pandas as pd

# Sample student data
data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Cathy', 'David', 'Eva'],
    'Age': [20, 21, 19, 22, 20],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Grade': ['A', 'B', 'B', 'A', 'A']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('student_info.csv', index=False)