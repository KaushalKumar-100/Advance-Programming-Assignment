class OrderService:
    def __init__(self,payment,notification,storage):
        self.payment=payment
        self.notification=notification
        self.storage=storage
        
    def placeOrder(self,order):
        self.payment.ProcessPayment()
        self.notification.sendNotification()
        self.storage.save(order)
        
        print("Order Placed Succesfully")