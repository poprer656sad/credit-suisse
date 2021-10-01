#!/bin/python3

import math

def portfolio_profit_maximisation(maxSum, a, b):
    if maxSum <= 0:
        return -math.inf
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return max(0, 1 + portfolio_profit_maximisation(maxSum-b.pop(0), [], b))
    if len(b) == 0:
        return max(0, 1 + portfolio_profit_maximisation(maxSum-a.pop(0), [], a))
    la = a.copy()
    aval = a.pop(0)
    lb = b.copy()
    bval = b.pop(0)
    if maxSum - aval < 0:
        return max(0, 1 + portfolio_profit_maximisation(maxSum-bval, la, b))
    if maxSum - bval < 0:
        return max(0, 1 + portfolio_profit_maximisation(maxSum-aval, la, b))
    return 1 + max(portfolio_profit_maximisation(maxSum-aval, a, lb), portfolio_profit_maximisation(maxSum-bval, la, b))

def main():
    first_multiple_input = input().rstrip().split()

    maxSum = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = portfolio_profit_maximisation(maxSum, a, b)

    print(result)

if __name__ == '__main__':
    main()