from datetime import datetime
class OrderType:
    
    def __init__(self,amount):
        
        self.amount=amount
        self.orderId=datetime.now().strftime("%y%m%d%H%M%S")
        
class RegularOrder(OrderType):
    pass

class DiscountedOrder(OrderType):
    def getDiscount(self):
        return self.amount*0.9
        
class PriorityOrder(OrderType):
    pass
        