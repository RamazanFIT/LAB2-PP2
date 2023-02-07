class Account:
    def __init__(p1, Name: str, Surname: str, Balance: int):
        p1.name_surname = Name + "_" +Surname
        p1.balance = Balance
    def deposit(self, money: int):
        self.balance += money 
    def balance_check(self):
        print("Balance:", self.balance, "tenge")
    def withdraw(self, How_much: int):
        if self.balance - How_much <= 0:
            print("No money in the deposit")
        else:
            self.balance -= How_much
        
# p1 = Account("Ramazan", "Syrlybay", 100)
# p1.balance_check()
# p1.deposit(12)
# p1.withdraw(10)
# p1.balance_check()




