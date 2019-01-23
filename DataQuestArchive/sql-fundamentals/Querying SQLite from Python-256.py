## 3. Connecting to the Database ##

import sqlite3

conn = sqlite3.connect("jobs.db")


## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "SELECT Major FROM recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
five_results = conn.execute("SELECT Major,Major_category FROM recent_grads").fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

conn = sqlite3.connect("jobs2.db")
reverse_alphabetical = conn.execute("SELECT Major\
                                    FROM recent_grads\
                                    ORDER BY Major DESC"
                                   ).fetchall()
conn.close()