class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., 'John Lee')
        bank the name of the bank (e.g., 'DBS')
        acnt the acount identifier (e.g., '5391 0375 9387 5309')
        limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._amt_owned = 0
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    def get_account(self):
        """Return the card identifying number (typically stored as a
        string)."""
        return self._account
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    def get_amt_owned(self):
        """Return current balance."""
        return self._amt_owned
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit
        limit.
        Return True if charge was processed; False if charge was
        denied.
        """
        if price + self._amt_owned > self._limit: # if charge would

            return False # cannot accept charge
        else:
            self._amt_owned += price
            return True # charge was accepted
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._amt_owned -= amount
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Lee', 'DBS',
    '5391 0375 9387 5309', 2500) )
    wallet.append(CreditCard('John Lee', 'OCBC',
    '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Lee', 'Maybank',
    '5391 0375 9387 5309', 5000) )    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Amt owned =', wallet[c].get_amt_owned ())
        while wallet[c].get_amt_owned () > 100:
            wallet[c].make_payment(100)
            print('New amt owned =', wallet[c].get_amt_owned ())
        print()
