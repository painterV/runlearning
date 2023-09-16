import pandas as pd
import sqlite3

# Create a sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'age': [25, 30, 22, 27, 29],
    'grade': [85.5, 92.3, 78.9, 88.1, 95.0]
}
df = pd.DataFrame(data)

# Connect to the SQLite database
conn = sqlite3.connect('student_info.db')

# Use the to_sql method to insert the DataFrame into the database
# The 'index' parameter specifies whether to include the DataFrame index as a column
df.to_sql('students', conn, if_exists='replace', index=False)

# Close the connection to the database
conn.close()