class Account:
    def __init__(self,bal,acco):
        self.balance=bal
        self.account=acco
    def debit(self,amount):
         self.balance-=amount
         print("Rs",amount,"is debited")
         print("Your new balance is",self.getbal())
    def credit(self,amount):
         self.balance+=amount
         print("Rs",amount,"is credited")
         print("Your new balance is",self.getbal())
    def getbal(self):
         return self.balance  
My_account=Account(45000,12341637)
My_account.debit(444)
My_account.credit(451)            