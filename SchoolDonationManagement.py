import mysql.connector

# Connecting to the MySQL database

conn = mysql.connector.connect(
    host="keshavpc",
    user="root",
    password="km2606@MySQL",
    database="schooldonationmanagementdb"
)

# Creating cursor object to interact with the database
cursor = conn.cursor()

# If want to create table from here
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS YourTableName (
#         ID INT AUTO_INCREMENT PRIMARY KEY,
#         Name VARCHAR(255),
#         PhoneNumber VARCHAR(10),
#         Email VARCHAR(255)
#     )
# ''')

def insert_data(table):
    if table == 'Donors':
        Name = input("Donor Name: ")
        Email = input("Donor Email: ")
        Phone = input("Donor Contact No. : ")
        Address = input("Donor Address: ")
        insert_query = f"INSERT INTO {table} (DonorName, Email, Phone, Address) VALUES ('{Name}', '{Email}', '{Phone}', '{Address}')"
        cursor.execute(insert_query)
        conn.commit()
        
    elif table == 'Receivers':
        Name = input("Receiver Name: ")
        Email = input("Receiver Email: ")
        Phone = input("Receiver Contact No. : ")
        Address = input("Receiver Address: ")
        insert_query = f"INSERT INTO {table} (ReceiverName, Email, Phone, Address) VALUES ('{Name}', '{Email}', '{Phone}', '{Address}')"
        cursor.execute(insert_query)
        conn.commit()

    elif table == 'Donated_items':
        Name = input("Item Name: ")
        description = input("Item Description: ")
        donorId = int(input("Donor Id: "))
        receiverId = int(input("Receiver Id: "))
        qty = int(input("Item Quantity: "))
        date = input("Donation Date: ")
        insert_query = f"INSERT INTO {table} (ItemName, ItemDescription, DonorID, ReceiverID, Quantity, DonationDate) VALUES ('{Name}', '{description}','{donorId}', '{receiverId}', '{qty}', '{date}')"
        cursor.execute(insert_query)
        conn.commit()

    elif table == 'Available_items':
        cursor.execute("SELECT ItemID FROM Donated_items")
        rows = cursor.fetchall()
        for _id in rows:
            available_qty = int(input(f"Quantity Available for {_id}: "))
        insert_query = f"INSERT INTO {table} (Available_qty) VALUES ('{available_qty}') WHERE ItemID = '{_id}'"
        cursor.execute(insert_query)
        conn.commit()

def delete_data(table):
    id = int(input("ID of row want to delete: "))
    if table == 'Donors':
        delete_query = f"DELETE FROM {table} WHERE DonorID = '{id}'"
        cursor.execute(delete_query)
        conn.commit()

    elif table == 'Receivers':
        delete_query = f"DELETE FROM {table} WHERE ReceiverID = '{id}'"
        cursor.execute(delete_query)
        conn.commit()

    elif table == 'Donated_items':
        delete_query = f"DELETE FROM {table} WHERE ItemID = '{id}'"
        cursor.execute(delete_query)
        conn.commit()

def update_data(table):
    if table == 'Donors':
        while True:
            print("1. ID")
            print("2. Donor Name")
            print("3. ")
            attr = input("Attributes to Update: ")
    update_query = f"UPDATE {table} "

def show_table(table):
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

n1, n2 = 0, 0;
while n1 < 5:
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Update Data")
    print("4. Show Table")
    print("5. Exit")
    n1 = int(input("Enter your Selection: "))
    if n1 >= 5:
        conn.close()
        break

    print("Select Table:")
    print("1. Donors")
    print("2. Receivers")
    print("3. Donated_items")
    print("4. Available_items")
    n2 = int(input("Enter your Selection: "))
    if n2 == 1:
        table = 'Donors'
    elif n2== 2:
        table = 'Receivers'
    elif n2 == 3:
        table = 'Donated_items'
    elif n2 == 4:
        table = 'Available_items'
    else:
        Print("Wrong Selection")

    if n1 == 1:
        insert_data(table)
    elif n1 == 2:
        delete_data(table)
    elif n1 == 3:
        update_data(table)
    elif n1 == 4:
        show_table(table)
