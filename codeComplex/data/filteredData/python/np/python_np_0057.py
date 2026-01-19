from math import factorial
from decimal import Decimal

def main(n):
    # Deterministic construction of A and B based on n
    # A: length n, alternating '+' and '-'
    A = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    # B: length n, positions:
    #   i % 3 == 0 -> '+'
    #   i % 3 == 1 -> '-'
    #   i % 3 == 2 -> '?'
    B = ''.join('+' if i % 3 == 0 else '-' if i % 3 == 1 else '?' for i in range(n))

    a = 0
    cnt2 = 0
    cnt1 = 0
    b = 0
    for i in A:
        if i == '+':
            a += 1
            cnt1 += 1
        else:
            a -= 1
            cnt2 += 1
    cnt3 = 0
    cnt = 0
    cnt4 = 0
    for i in B:
        if i == '+':
            b += 1
            cnt3 += 1
        elif i == '-':
            b -= 1
            cnt4 += 1
        else:
            cnt += 1
    if cnt3 > cnt1 or cnt4 > cnt2:
        print(format(0, '.12f'))
    else:
        No_of_plus = cnt1 - cnt3
        No_of_minus = cnt2 - cnt4
        Total_cases = 2 ** cnt
        Total_No_of_favourable_cases = factorial(cnt) // (factorial(No_of_plus) * factorial(No_of_minus))
        print(format(Decimal(Total_No_of_favourable_cases) / Decimal(Total_cases), '.12f'))


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)