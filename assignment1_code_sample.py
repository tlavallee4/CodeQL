import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # Starting a process with a shell, command injection without proper sanitization.
    # Attacker can control any of the to, subject, body with malicious shell commands (delete system files)
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # Uses HTTP instead of HTTPS - data not encrypted and can be modified by attackers
    url = 'http://insecure-api.com/get-data'
    # urlopen can be used to get local files
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    # SQL query allows attackers to manipulate the database, delete, modify
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
