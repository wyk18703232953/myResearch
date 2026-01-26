import math

def main(n):
    # Deterministically generate two strings s and s2 of length n
    # s has a pattern: first n//2 are '+', rest are '-'
    half = n // 2
    s = "+" * half + "-" * (n - half)
    # s2 alternates between '+' and '-'
    s2 = "".join("+" if i % 2 == 0 else "-" for i in range(n))

    p = s.count("+")
    m = s.count("-")
    q = s2.count("+")
    w = s2.count("-")
    pr, mr = p - q, m - w

    if pr < 0 or mr < 0:
        print("{:.12f}".format(0.0))
    else:
        temp = pr + mr
        if temp == 0:
            print("{:.12f}".format(1.0))
        else:
            i = 2 ** temp
            res = math.factorial(temp) / (math.factorial(pr) * math.factorial(mr))
            ans = res / i
            print("{:.12f}".format(ans))


if __name__ == "__main__":
    main(10)