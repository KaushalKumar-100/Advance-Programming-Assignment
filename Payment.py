class Payment:
    def __init__(self,amount):
        self.amount=amount
        
    def ProcessPayment(self):
        pass

class CreditCard(Payment):
    def __init__(self,amount,creditcard):
        super().__init__(amount)
        self.creditcard=creditcard  
    def ProcessPayment(self):
        print(f" {self.amount} has been paid using creditcard")
    
        
class UPI(Payment):
    def __init__(self,amount,upi):
        super().__init__(amount)
        self.upi=upi
    def ProcessPayment(self):
        print(f" {self.amount} has been paid using upi")

class Wallet(Payment):
    def __init__(self,amount,wallet):
        super().__init__(amount)
        self.wallet=wallet
    def ProcessPayment(self):
        print(f" {self.amount} has been paid using wallet")