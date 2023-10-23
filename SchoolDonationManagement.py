import mysql.connector
from mysql.connector import errorcode

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
        donorId = int(input("Donor Id: "))
        receiverId = int(input("Receiver Id: "))
        qty = int(input("Item Quantity: "))
        date = input("Donation Date: ")
        insert_query = f"INSERT INTO {table} (ItemName, Donated_qty, DonorID, ReceiverID, DonationDate) VALUES ('{Name}', '{qty}', '{donorId}', '{receiverId}', '{date}')"
        cursor.execute(insert_query)
        conn.commit()

    elif table == 'Available_items':
        id = int(input("Item Id: "))
        available_qty = int(input(f"Quantity Available: "))
        insert_query = f"INSERT INTO {table} (ItemID, Available_qty) VALUES ('{id}','{available_qty}')"
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


def show_table(table):
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



# Connecting to the MySQL database
try:
    conn = mysql.connector.connect(
        host="keshavpc",
        user="root",
        password="km2606@MySQL",
        database="schooldonationmanagementdb"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist")
    else:
        print(f"Error: {err}")

# Creating cursor object to interact with the database
cursor = conn.cursor()

# If want to create table from here(Python Code)
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS YourTableName (
#         ID INT AUTO_INCREMENT PRIMARY KEY,
#         Name VARCHAR(255),
#         PhoneNumber VARCHAR(10),
#         Email VARCHAR(255)
#     )
# ''')

n1, n2 = 0, 0
while n1 < 4:
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Show Table")
    print("4. Exit")
    n1 = int(input("Enter your Selection: "))
    if n1 >= 4:
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
        show_table(table)