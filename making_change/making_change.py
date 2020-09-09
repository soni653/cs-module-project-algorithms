#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if cache is None:
    cache = {}

  if amount == 0 and amount < 5:
    return 1

  if amount < 0:
    return 0

  if cache and cache[amount]:
    return cache[amount]


  for coin in denominations:
    cache[amount] = making_change(amount-coin, denominations)

  return cache[amount]





    # return num_ways_to_make_change
    # for i in range(0, len(denominations)):
    #     for j in range(denominations[i], amount + 1):
    #         table[j] += table[j - denominations[i]]



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")