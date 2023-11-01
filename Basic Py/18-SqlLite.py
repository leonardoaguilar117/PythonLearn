import sqlite3

# Create db
with sqlite3.connect("D://MySQL Proyects/app.db") as connection:

    # Variable cursor to interact with db
    cursor = connection.cursor()
    phones = [
        (4041, "Huawei P100 XLPRO XL100", 8999),
        (3201, "Apple Iphone 12 PRO MAX", 23700.99),
        (1411, "Infinix HOT 30 256 GB", 3799.99)
    ]

    # Create table
    cursor.execute(
        """ CREATE TABLE phones(
            int INT(20) PRIMARY KEY,
            nombre VARCHAR(30),
            precio DECIMAL
        )
        """
    )

    # insert multiple values in phones
    cursor.executemany(
        """ INSERT INTO phones VALUES (?, ?, ?) 
        """, phones
    )

    # requests
    cursor.execute("SELECT * FROM phones")
    allTuples = cursor.fetchall()
    for rows in allTuples:
        print(rows)
