from math import factorial, pow

def compute_probability(s1, s2):
    S1 = {"+": 0, "-": 0}
    S2 = {"+": 0, "-": 0, "?": 0}
    for c in s1:
        S1[c] += 1
    for c in s2:
        S2[c] += 1
    if S1["+"] - S2["+"] >= 0 and S1["-"] - S2["-"] >= 0:
        pos = S1["+"] - S2["+"]
        neg = S1["-"] - S2["-"]
        ques = S2["?"]
        res = (factorial(pos + neg) / (factorial(pos) * factorial(neg))) / pow(2, ques)
        return "%.12f" % res
    else:
        return "%.12f" % 0.0

def main(n):
    # Input structure:
    # Original program reads two strings s1, s2 consisting of '+', '-', '?'
    # Here n controls the length of s1 and s2 in a deterministic way.

    if n <= 0:
        n = 1

    # Deterministic construction:
    # s1: first half '+', second half '-'
    # s2: pattern of '+', '-', '?' based on index
    half = n // 2
    s1 = ["+"] * half + ["-"] * (n - half)

    s2 = []
    for i in range(n):
        r = i % 3
        if r == 0:
            s2.append("+")
        elif r == 1:
            s2.append("-")
        else:
            s2.append("?")

    result = compute_probability(s1, s2)
    print(result)

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)