from collections import Counter

def f(x):
    return max(list(Counter(x).values()))

def v_gen(x, l):
    if x == l:
        return x - 1
    else:
        return x + 1

def run_logic(n, z, s_b, s_c):
    l = len(z)
    a = f(z)
    b = f(s_b)
    c = f(s_c)

    def v(x):
        return v_gen(x, l)

    if n == 1:
        a, b, c = v(a), v(b), v(c)
        if a > b and a > c:
            return "Kuro"
        elif b > a and b > c:
            return "Shiro"
        elif c > a and c > b:
            return "Katie"
        else:
            return "Draw"
    elif (l - a <= n) + (l - b <= n) + (l - c <= n) >= 2:
        return "Draw"
    elif a > b and a > c:
        return "Kuro"
    elif b > a and b > c:
        return "Shiro"
    elif c > a and c > b:
        return "Katie"
    else:
        return "Draw"

def generate_strings(l):
    # deterministic generation: cycle through fixed characters
    chars = "abc"
    def make(base_offset):
        return "".join(chars[(i + base_offset) % len(chars)] for i in range(l))
    z = make(0)
    s_b = make(1)
    s_c = make(2)
    return z, s_b, s_c

def main(n):
    if n < 1:
        n = 1
    # map n to string length; ensure length >= 1
    l = n
    z, s_b, s_c = generate_strings(l)
    result = run_logic(n, z, s_b, s_c)
    print(result)

if __name__ == "__main__":
    # example scalable call; adjust n as needed for experiments
    main(10)