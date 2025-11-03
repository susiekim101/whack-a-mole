from algo import coin_change


def test_coin_change_example():
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3

def test_non_greedy():
    coins = [5, 3]
    amount = 14
    assert coin_change(coins, amount) == 14