class BankAccount:
    def __init__(self, initialbalance = 0) :
         self.__account_balance = initialbalance 

    
    def deposit(self, amount) :
        if amount > 0:
            self.__account_balance += amount
    
    def withdraw(self, amount) :
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
        
    def display_balance(self) :
        print(f"your current balance is ${self.__account_balance}")
   