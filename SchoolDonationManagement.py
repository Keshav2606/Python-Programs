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

def insert_data(table):
    if table == 'Donors':
        id = int(input("Donor ID: "))
        Name = input("Donor Name: ")
        Email = input("Donor Email: ")
        Phone = input("Donor Contact No. : ")
        Address = input("Donor Address: ")
        insert_query = f"INSERT INTO {table} (DonorId, DonorName, Email, Phone, Address) VALUES ('{id}', '{Name}', '{Email}', '{Phone}', '{Address}')"
        cursor.execute(insert_query)
        
    elif table == 'Receivers':
        id = int(input("Receiver ID: "))
        Name = input("Receiver Name: ")
        Email = input("Receiver Email: ")
        Phone = input("Receiver Contact No. : ")
        Address = input("Receiver Address: ")
        insert_query = f"INSERT INTO {table} (ReceiverId, ReceiverName, Email, Phone, Address) VALUES ('{id}', '{Name}', '{Email}', '{Phone}', '{Address}')"
        cursor.execute(insert_query)

    elif table == 'Donated_items':
        id = int(input("Item ID: "))
        Name = input("Item Name: ")
        description = input("Item Description: ")
        qty = int(input("Item Quantity: "))
        date = input("Donation Date: ")
        insert_query = f"INSERT INTO {table} (ItemId, ItemName, ItemDescription, Quantity, DonationDate) VALUES ('{id}', '{Name}', '{description}', '{qty}', '{date}')"
        cursor.execute(insert_query)

    elif table == 'Available_items':
        available_qty = int(input("Quantity Available: "))
        insert_query = f"INSERT INTO {table} (Available_qty) VALUES ('{available_qty}')"
        cursor.execute(insert_query)

def delete_data(table):
    id = int(input("ID of row want to delete: "))
    if table == 'Donors':
        delete_query = f"DELETE FROM {table} WHERE DonorID = '{id}'"
        cursor.execute(delete_query)

    elif table == 'Receivers':
        delete_query = f"DELETE FROM {table} WHERE ReceiverID = '{id}'"
        cursor.execute(delete_query)

    elif table == 'Donated_items':
        delete_query = f"DELETE FROM {table} WHERE ItemID = '{id}'"
        cursor.execute(delete_query)



def show_table(table):
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

n1, n2 = 0, 0;
while True:
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Update Data")
    print("4. Show Table")
    print("5. Commit Changes")
    n1 = int(input("Enter your Selection: "))

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
    elif n1 == 5:
        conn.commit()
    else:
        Print("Wrong Selection")
