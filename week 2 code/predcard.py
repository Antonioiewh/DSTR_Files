from credit_card import CreditCard
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and
    fees."""
    def __init__(self, customer, bank, acnt, limit,apr):
        super().__init__(customer, bank, acnt, limit)
        self.__apr = apr

    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._amt_owned += 5.0 # assess $5 fee
        else:
            self._count +=1
            if self._count > 10:
                self._amt_owned += 1.0
    def process_month(self):
        """Assess monthly interest on the outstanding balance."""
        if self._amt_owned > 0:
            monthly_factor = pow(1 + self.__apr, 1/12.0)
            self._amt_owned *= monthly_factor


