from pymysql import connect
import os

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USERS'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
    )
""""
try:
    with connection.cursor() as cursor:
        query = "insert into accounts (account_holder, account_number, sort_code, deposit, withdrawals, balance) values ('Thomas Hurs', '67854389', '224455', '6057', '0', '6057')"
        cursor.execute(query)
    connection.commit()
"""

user_firstname = str(input("please enter your name: "))
user_lastname = str(input("please enter your lastname: "))
email =str(input("please enetr your email: "))

answer = str(input("Do you want to create an account?Y/N? \n"))

if answer == 'Y':
    try:
        with connection.cursor() as cursor:
            try:
    with connection.cursor() as cursor:
        query = "insert into accounts (account_holder, account_number, sort_code, deposit, withdrawals, balance)"
        cursor.execute(query)
    connection.commit()
"""
            
finally:
    connection.close()
       
       
"""
class Account:
    def __init__(self, account_holder, account_number, sort_code, account_year, deposit, withdrawal, balance,
                 account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.sort_code = sort_code
        self.account_year = account_year
        self.deposit = deposit
        self.withdraw = withdrawal
        self.balance = balance
        self.account_type = account_type


def display_account(self):
    print("account_holder:" + self.account_holder + "\n" + "account_number:" + self.account_number + "\n"
          + "sort_code:" + self.sort_code + "\n" + "account_year:" + self.account_year + "\n" + "deposit"
          + self.deposit + "\n" + "withdrawal:" + "\n" + "balance" + self.balance + "\n"
          + "account_type" + self.account_type)
        


class withdraw:
    def __init__(self, account_holder, account_number, sort_code,account_year,
                 deposit, withdrawal, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.sort_code = sort_code
        self.account_type = account_type

"""
