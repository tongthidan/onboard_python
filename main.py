# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import mariadb as mariadb


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_user(cur):
    users = [];
    hotels = [];
    # cur.execute("SELECT user_id, name, link FROM rs_user_behavior.tbluser")
    cur.execute("SELECT hotel_id, name, address FROM rs_user_behavior.tblhotel")
    # Prepare Contacts
    # for (user_id, name, link) in cur:
    #     users.append(f"{user_id} {name} <{link}>")
    for (hotel_id, name, address) in cur:
        hotels.append(f"{hotel_id} {name} <{address}>")

    # List Contacts
    totalUser = len(hotels)
    print(totalUser)


try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        host="localhost",
        port=3306)

    # Instantiate Cursor
    cur = conn.cursor()

    print_user(cur)

    # Close Connection
    conn.close()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Enterprise: {e}")
    sys.exit(1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
