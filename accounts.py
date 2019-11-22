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
        
