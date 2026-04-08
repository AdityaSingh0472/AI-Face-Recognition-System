import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

#DATABASE FUNCTIONS
def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_user(name, age):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()


def get_user(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE name=?", (name,))
    data = cursor.fetchone()

    conn.close()
    return data


#ENTRY–EXIT SYSTEM
def mark_entry_exit(name):
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    try:
        with open("attendance.csv", "r") as f:
            lines = f.readlines()
    except:
        lines = []

    user_today = [line for line in lines if name in line and today in line]

    if len(user_today) == 0:
        with open("attendance.csv", "a") as f:
            f.write(f"{name},{today},IN,{time_now}\n")
        print("Entry marked")

    elif len(user_today) == 1:
        with open("attendance.csv", "a") as f:
            f.write(f"{name},{today},OUT,{time_now}\n")
        print("Exit marked")


#EMAIL ALERT (5 IMAGES)
def send_alert(image_paths):
    sender_email = "aditya.singh0472@gmail.com"
    app_password = "ultjulyjzbgzlxgn"
    receiver_email = "singh.aditya4714@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "🚨 Unknown Person Detected"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msg.set_content("Unknown person detected. Images attached.")

    try:
        for image_path in image_paths:
            if os.path.exists(image_path):
                with open(image_path, "rb") as f:
                    file_data = f.read()
                    file_name = os.path.basename(image_path)

                msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        print("✅ Email sent successfully (5 images)")

    except Exception as e:
        print("❌ Email failed:", e)