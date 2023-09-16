import sqlite3

# Connect to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('comments.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

#[1, 172372338768, '450777347', 'BV16k4y1T7qe', 742798870, '-白莫-', 5, 'https://i2.hdslb.com/bfs/face/8e4ba1395f3c4b48aa1f1884b1d09742ce0652a9.jpg', '2023-06-29 22:47:25', '纯纯健身小白，从来没健身过那种，暑假打算拿出两个月时间健身，目前身高体重183/154，大概能练成什么状态，然后就是想问下各位大佬有没有什么建议[妙啊]']

#count, rpid, mid, bv, aid, nickname, level, avatar, comment_time, content

# Define the SQL command to create a table
create_table_sql = '''
CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    rpid INTEGER,
    mid TEXT NOT NULL,
    bv VACHAR(20),
    aid INTEGER,
    nickname TEXT,
    level INTEGER,
    avatar TEXT,
    comment_time DATETIME,
    message TEXT,
    root INTEGER,
    parent INTEGER
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_sql)

# Save (commit) the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
