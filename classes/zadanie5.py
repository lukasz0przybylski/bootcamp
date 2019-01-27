class CashMachine:
    # is_availble = False

    @property
    def is_avaible(self):

        return False

    def put_money(self, bills_list):
        self.money.extend(bills_list)

    def withrow_monay(self,amount):
        monay_to_whitrow = []
        for bill in sorted(self, money, reverse=True):
            if sum(monay_to_whitrow) + bill <= amount:
                monay_to_whitrow.append(bill)
        # tu sprawdzam czy udało sie uzbierac hajsu ile trzeba
        if sum(monay_to_whitrow) != amount:
            return
        #
        for bill in monay_to_whitrow:
            self.money.remove(bill)

        return monay_to_whitrow




def test_cash_nachine_is_not_avaible():
    cash_machine = CashMachine()

    assert not cash_machine.is_avaible()


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_avaible

def test_withrow_monay():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine