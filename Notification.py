class Notification:
    def __init__(self,amount):
        self.amount=amount
    def sendNotification(self):
        pass
        
class Gmail(Notification):
    def __init__(self,amount,gmail):
        super().__init__(amount)
        self.gmail=gmail
    def sendNotification(self):
        print(f"Email has been to {self.gmail}: the amount{self.amount}has been debited from your account")
        
class SMS(Notification):
    def __init__(self,amount,phoneNr):
        super().__init__(amount)
        self.phoneNr=phoneNr
    def sendNotification(self):
        print(f"message has been sent to your {self.phoneNr} has been debited amount {self.amount}")