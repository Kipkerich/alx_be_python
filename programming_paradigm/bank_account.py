class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
        
    def deposit(self, amount):
            return  self. account_balance + amount
    def withdraw(self, amount):
            if (self.account_balance - amount) <= 0:
                return False
            else:
                return True
        
    def display_balance():
            return print(f"Current Balance: ${BankAccount}")
        

        
        
