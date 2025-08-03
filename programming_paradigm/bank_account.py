class BankAccount:
    def __init__(self, currentbalance = 0) :
         self.__account_balance = currentbalance 

    
    def deposit(self, amount) :
        if amount > 0:
            self.__account_balance += amount
    
    def withdraw(self, amount) :
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
        
    def display_balance(self) :
        print(f"Current Balance:  ${self.__account_balance}")
   