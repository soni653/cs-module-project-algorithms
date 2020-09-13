#!/usr/bin/python

import sys

def making_change(amount, denominations):
    # intializes list with 0 of sze ammoutn
    cache = [0 for _ in range(amount + 1)]
    # one way to get zero coins
    cache[0] = 1
    # for each denominatio of coin
    for coin_value in denominations:
        # consider each coin value at a time
        for amt in range(1, amount + 1):
            diff_amount = amt - coin_value
            if diff_amount >= 0:
                # how many ways do we know how to make diff_amount (so far)?
                ways_to_make_diff_amount = cache[diff_amount]
                # we know we can make amt by adding the current coin value to any of the ways we make diff_amount,
                # in addition to all the ways we've found to make amt with other coin values
                cache[amt] = cache[amt] + ways_to_make_diff_amount
    return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")