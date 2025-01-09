import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.balance = 1000  # Initial balance

        # Create UI components
        self.label = tk.Label(master, text="Welcome to the ATM", font=("Arial", 16))
        self.label.pack(pady=10)

        self.balance_label = tk.Label(master, text=f"Current Balance: ${self.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.amount_label = tk.Label(master, text="Enter Amount:", font=("Arial", 12))
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.check_balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"${amount} deposited successfully!")
                self.amount_entry.delete(0, tk.END)
                self.update_balance()
            else:
                messagebox.showwarning("Warning", "Please enter a positive amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    messagebox.showinfo("Success", f"${amount} withdrawn successfully!")
                    self.amount_entry.delete(0, tk.END)
                    self.update_balance()
                else:
                    messagebox.showwarning("Warning", "Insufficient balance.")
            else:
                messagebox.showwarning("Warning", "Please enter a positive amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def update_balance(self):
        self.balance_label.config(text=f"Current Balance: ${self.balance}")

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
