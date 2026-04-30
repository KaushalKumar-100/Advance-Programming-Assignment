/*Design a banking system in Java with:

A base class Account containing private fields: accountNumber, ownerName, balance
Provide getters/setters and at least two constructors (use constructor chaining)
Implement deposit() and withdraw() with proper validation
Add a display() method

Extend it with:

SavingsAccount (add interestRate, override display() and show interest)
CurrentAccount (add overdraftLimit, restrict withdrawals accordingly)

Your implementation should clearly show:

Proper encapsulation (no direct field access)
Use of constructor overloading and chaining (this(...))
Inheritance and method overriding (use @Override and super)
Polymorphism by storing objects in an Account reference list and calling display()
Basic validation/debugging (e.g., assert or exception for invalid operations)*/


import java.util.*;

class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Constructor 1
    Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = balance;
    }

    // Constructor 2 (Constructor Chaining)
    Account() {
        this("0000", "Default User", 0.0);
    }

    // Getters
    public String getAccountNumber() {
        return this.accountNumber;
    }

    public String getOwnerName() {
        return this.ownerName;
    }

    public double getBalance() {
        return this.balance;
    }

    // Setters
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        } else {
            System.out.println("Invalid balance");
        }
    }

    // Withdraw Method
    public void withdrawal(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount");
        } 
        else if (this.balance >= amount) {
            System.out.println("Your account " + this.accountNumber +
                    " is debited with " + amount);
            this.balance -= amount;
        } 
        else {
            System.out.println("Insufficient balance");
        }
    }

    // Deposit Method
    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid deposit amount");
        } 
        else {
            System.out.println("Your account " + this.accountNumber +
                    " is credited with " + amount);
            this.balance += amount;
        }
    }

    // Display Method
    public void display() {
        System.out.println("Account Number: " + this.accountNumber);
        System.out.println("Owner Name: " + this.ownerName);
        System.out.println("Current Balance: " + this.balance);
    }
}


class SavingsAccount extends Account {
    private float interestRate;

    SavingsAccount(String accountNumber, String ownerName,
                   double balance, float interestRate) {
        super(accountNumber, ownerName, balance);
        this.interestRate = interestRate;
    }

    public void interest() {
        double s = (getBalance() * 1 * this.interestRate) / 100;
        System.out.println("Yearly Interest Generated: " + s);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Interest Rate: " + this.interestRate + "%");
        interest();
    }
}


class CurrentAccount extends Account {
    private double overdraftLimit;

    CurrentAccount(String accountNumber, String ownerName,
                   double balance, double overdraftLimit) {
        super(accountNumber, ownerName, balance);
        this.overdraftLimit = overdraftLimit;
    }

    // Override withdrawal for overdraft feature
    @Override
    public void withdrawal(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount");
        } 
        else if (getBalance() + overdraftLimit >= amount) {
            System.out.println("Your account " + getAccountNumber() +
                    " is debited with " + amount);
            setBalance(getBalance() - amount);
        } 
        else {
            System.out.println("Overdraft limit exceeded");
        }
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: " + this.overdraftLimit);
    }
}


public class banking_system {
    public static void main(String[] args) {

        // Polymorphism using Account reference list
        ArrayList<Account> accounts = new ArrayList<>();

        Account a1 = new SavingsAccount(
                "ACC101",
                "Kaushal",
                10000,
                5.5f
        );

        Account a2 = new CurrentAccount(
                "ACC102",
                "Rahul",
                5000,
                2000
        );

        accounts.add(a1);
        accounts.add(a2);

        // Deposit and Withdraw
        a1.deposit(2000);
        a1.withdrawal(3000);

        a2.deposit(1000);
        a2.withdrawal(6500);

        System.out.println("\nAccount Details ");

        // Runtime Polymorphism
        for (Account acc : accounts) {
            acc.display();
            System.out.println("-------------------");
        }
    }
}