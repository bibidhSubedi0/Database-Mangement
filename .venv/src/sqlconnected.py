import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ilovenepal",
    database="psql"
)
mycursor = conn.cursor()



# print("All tables :")
# for rows in results:
#     print(rows)

# mycursor.execute("""
#     CREATE TABLE clients(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), department VARCHAR(30),money_spend INT)
# """)
# sql = "INSERT INTO employees (name, department) VALUES (%s, %s)"
# values = [("Ram","kalimati"),("Sita","Rammechhap")]
# mycursor.executemany(sql, values)
# conn.commit()
#
# print(mycursor.rowcount, "rows inserted.")

print("\nEmployee Data :")
mycursor.execute("SELECT * FROM employees")
results = mycursor.fetchall()
for rows in results:
    print(rows)
