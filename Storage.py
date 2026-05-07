class Storage:
    def save(self,order):
        pass
    
class Database(Storage):
    def save(self,order):
        print(f"order {order.orderId} has been saved to your data base")

class File(Storage):
    def save(self,order):
        print(f"order {order.orderId} has been saved to your file")