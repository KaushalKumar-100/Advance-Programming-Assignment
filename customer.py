'''Assignment 12: 
Design a system in java/python for processing customer orders in an e-commerce platform. 

An order system should support:

Multiple payment methods (Credit Card, UPI, Wallet, etc.)
Multiple notification channels (Email, SMS, Push)
Different order types (Regular Order, Discounted Order, Priority Order)
Ability to store order data using different storage mechanisms (Database, File, etc.)
Design Constraints (Must Apply SOLID Principles)

Your design must satisfy the SOLID principles as follows:

1. Single Responsibility Principle (SRP): Each class should have a single responsibility
(e.g., order logic, payment processing, notification, storage should be separate)

2. Open/Closed Principle (OCP): You should be able to add:
New payment methods
New notification types
Without modifying existing classes

3. Liskov Substitution Principle (LSP): All subclasses (e.g., payment types, order types) should work correctly when used through their base type, No subclass should break expected behavior

4. Interface Segregation Principle (ISP): Avoid large interfaces, Design small, role-specific interfaces
(e.g., don’t force all classes to implement unused methods)

5. Dependency Inversion Principle (DIP): High-level classes (e.g., OrderService) must depend on abstractions, not concrete implementations, Use dependency injection.

Your system should:

Create an order,
Process payment using a selected payment method,
Send notification after successful order,
Save order details using a storage mechanism;'''
from OrderType import OrderType, RegularOrder, DiscountedOrder, PriorityOrder
from Payment import CreditCard, UPI, Wallet
from Notification import Gmail,SMS
from Storage import Database, File
from OrderService import OrderService


#creating object



#selecting order type

Ordertype = {
    "regularorder": RegularOrder,
    "discountedorder": DiscountedOrder,
    "priorityorder": PriorityOrder
}

print("Please select your Order Type from given list:\n")
print(list(Ordertype.keys()))

order = input().lower()

tempOrder = None

if order in Ordertype:
    tempOrder = Ordertype[order]
else:
    print("Invalid Order Type")


print("Enter the Amount of Order:")
amount = float(input())



#selecting payment type

paymentype = {
    "creditcard": CreditCard,
    "upi": UPI,
    "wallet": Wallet
}

print("Please select your Payment Type from given list:\n")
print(list(paymentype.keys()))

payment = input().lower()

temppayment = None
cardNumber = None

if payment in paymentype:
    temppayment = paymentype[payment]

    if payment == "creditcard":
        print("Enter your Credit Card Number:")
        cardNumber = input()

    elif payment == "upi":
        print("Enter your UPI ID:")
        cardNumber = input() + "@upi"

    elif payment == "wallet":
        print("Enter your Wallet Number:")
        cardNumber = input()

else:
    print("Invalid Payment Type")



#selecting notification type

notificationtype = {
    "gmail": Gmail,
    "sms": SMS
}

print("Please select your Notification Type:\n")
print(list(notificationtype.keys()))

notification = input().lower()

tempNotification = None
messagetype = None

if notification in notificationtype:
    tempNotification = notificationtype[notification]

    if notification == "gmail":
        print("Enter your Gmail ID:")
        messagetype = input() + "@gmail.com"

    elif notification == "sms":
        print("Enter your Phone Number:")
        messagetype = input()

else:
    print("Invalid Notification Type")



#object creation

order1 = tempOrder(amount)

payment1 = temppayment(amount, cardNumber)

notification1 = tempNotification(amount, messagetype)

storage1 = Database()

service = OrderService(payment1, notification1, storage1)

service.placeOrder(order1)