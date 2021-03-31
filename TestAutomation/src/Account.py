class Account():
    money = 0;
    def _init_(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount


account = Account()
money = 100 
account.deposit(50)
print(money, account.money)
