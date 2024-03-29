class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """Create a credit card instance
        The initial balance is 0"""

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    
    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_account(self):
        """Return card ID"""
        return self._account
    
    def get_limit(self):
        """Return limit of the account"""
        return self._limit

    def get_balance(self):
        """Return balance of the account"""
        return self._balance

    def charge(self, price):
        """Charge to the account given a price"""
        if price + self._balance > self._limit:
            return False
        else: self._balance += price
        return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        elif amount < 0:
            raise ValueError("amount cant be negative")                           
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard( "John Bowman","California Savings","5391 0375 9387 5309", 2500))
    wallet.append(CreditCard( "John Bowman","California Federal","3485 0399 3395 1954", 3500))
    wallet.append(CreditCard( "John Bowman","California Finance" ,"5391 0375 9387 5309" , 5000))


    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)

    for c in range(3):
        print('customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New Balance = ", wallet[c].get_balance())

    print(wallet[0].get_balance())


class PredatoryCreditCard(CreditCard):
    """An extension to Credit Card that compounds interests and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """"Charge given price to the card, assuming sufficient credit limit
        Return True if charge was precessed.
        Return False and assess $5 fee if charge is denied"""

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
