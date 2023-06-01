from bankaccount import *
import pytest
def test_withdraw():
    assert withdraw(2000, 4000) == 2000
    assert withdraw(4245, 1345) == False
    assert withdraw(3000, 6000) == 3000
    assert withdraw(1000, 1000) == 0


def test_transfer_amount():
    assert transfer_amount(1000, 2000) == 1000
    assert transfer_amount(4000, 2000) == False
    assert transfer_amount(1000, 1000) == 0


def test_print_account_details():
    print_account_details("Moh", "Tigani", "USD", 7000)
    # Expected output:
    # Name: Moh Tigani
    # Balance: 7000
    # Currency: USD
