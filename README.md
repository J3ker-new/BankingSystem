# 🏦 BankAccounts OOP Project (Python)

A simple bank account management system using Python and Object-Oriented Programming (OOP) concepts.

---

## 🚀 Features

- **Account Creation** (with minimum balance requirement)
- **Deposit & Withdraw** (with transaction history)
- **Transaction History** for each account
- **Account Summary** (view recent transactions and balance)
- **View All Account Data**
- **Account Deletion**
- **Total Account Counter**
- **User-friendly Console Output**

---

## 📦 File Structure

```text
bank_accounts.py   # Main program file with all class definitions and usage examples
README.md          # You're reading it!
```

---

## 📝 Example Usage

```python
from bank_accounts import BankAccounts

# Greet new customers
BankAccounts.greet()

# Create a new account
acc1 = BankAccounts("Chirag", 15000)

# Deposit and withdraw
acc1.deposit(1000)
acc1.withdraw(500)

# View account details
acc1.showData()

# Show transaction history
acc1.showHistory()

# Show account summary
acc1.acc_summary()

# Delete account
BankAccounts.deleteAcc(acc1.account_number)
```

---

## 💡 Concepts Demonstrated

- Python Classes & Objects
- Class Methods vs. Static Methods
- Instance Methods and Attributes
- Dictionaries for Object Storage
- Exception Handling
- Transaction Logging

---

## 🏁 Getting Started

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/bank-oop-python.git
    cd bank-oop-python
    ```

2. Run the script:
    ```bash
    python bank_accounts.py
    ```

---

## ⚙️ Customization

- Change the minimum opening balance by editing the check in `__init__`.
- Add more features like interest calculation, account types, etc.

---

## 🤓 Author Notes

This project marks my transition from Java to Python (and OOP in Python)!  
Stay tuned for more as I revisit Java and explore Spring Boot soon.

---

## 📄 License

MIT License
