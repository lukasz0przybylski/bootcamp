class CashMachine:
    # is_availble = False

    @property
    def is_avaible(self):

        return False

    def put_money(self, bills_list):
        self.money.extend(bills_list)


def test_cash_nachine_is_not_avaible():
    cash_machine = CashMachine()

    assert not cash_machine.is_avaible()


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cas