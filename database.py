import sqlite3
import os

def init_db():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_password(service, username, encrypted_password, salt):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, encrypted_password, salt) VALUES (?, ?, ?, ?)",
        (service, username, encrypted_password, salt)
    )
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, service, username, encrypted_password, salt FROM passwords")
    data = cursor.fetchall()
    conn.close()
    return data

def delete_password(password_id):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
    conn.commit()
    conn.close()