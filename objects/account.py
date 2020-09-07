class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            raise ValueError(
                "Cannot withdraw %d from account with balance of %d"
                % (amount, self.balance)
            )
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def add_interest(self, interest_rate):
        if self.type == "savings":
            self.balance *= 1 + interest_rate
