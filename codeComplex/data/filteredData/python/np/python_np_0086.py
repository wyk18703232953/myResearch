import math

def main(n):
    # Generate deterministic s1 and s2 based on n
    # s1: first n positions, alternating '+' and '-'
    s1 = "".join('+' if i % 2 == 0 else '-' for i in range(n))
    # s2: first n positions, cycle '+', '-', '?'
    pattern = ['+', '-', '?']
    s2 = "".join(pattern[i % 3] for i in range(n))

    s1p = s1.count("+")
    s1m = s1.count("-")
    s2p = s2.count("+")
    s2m = s2.count("-")
    s2q = 0
    if '?' in s2:
        s2q = s2.count("?")
    if s2q == 0:
        if s1p == s2p and s1m == s2m:
            print("%.12f" % 1)
        else:
            print("%.12f" % 0)
    else:
        if s1p >= s2p and s1m >= s2m:
            s2q = math.factorial(s2q) / (math.factorial(s1p - s2p) * math.factorial(s1m - s2m))
            print("%.12f" % (s2q / (2 ** s2.count("?"))))
        else:
            print("%.12f" % 0)


if __name__ == "__main__":
    main(10)