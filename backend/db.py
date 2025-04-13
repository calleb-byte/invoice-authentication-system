
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="invoiceauthentication"
    )

def insert_invoice(data):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO invoices (invoice_number, client_name, amount, phone_number) VALUES (%s, %s, %s, %s)"
    values = (data['invoice_number'], data['client_name'], data['amount'], data['phone_number'])
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.lastrowid
