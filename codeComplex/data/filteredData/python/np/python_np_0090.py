from math import factorial

def compute_probability(s1, s2):
    p = 0
    m = 0
    blank = 0
    for i in range(len(s1)):
        if s1[i] == "+":
            p += 1
        else:
            m += 1
        if s2[i] == "+":
            p -= 1
        elif s2[i] == "-":
            m -= 1
        else:
            blank += 1
    if m < 0 or p < 0:
        return 0.0
    if m == 0:
        return 0.5 ** p
    if p == 0:
        return 0.5 ** m
    b = blank
    return (factorial(b) / factorial(p) / factorial(m)) * (0.5 ** b)

def generate_input(n):
    if n <= 0:
        return "+", "+"
    s1 = []
    s2 = []
    for i in range(n):
        if i % 2 == 0:
            s1.append("+")
        else:
            s1.append("-")
        r = i % 3
        if r == 0:
            s2.append("+")
        elif r == 1:
            s2.append("-")
        else:
            s2.append("?")
    return "".join(s1), "".join(s2)

def main(n):
    s1, s2 = generate_input(n)
    ans = compute_probability(s1, s2)
    print(ans)

if __name__ == "__main__":
    main(10)