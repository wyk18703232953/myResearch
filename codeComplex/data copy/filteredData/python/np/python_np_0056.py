import math

def main(n):
    # Interpret n as the length of string s
    # Construct deterministic t and s following the same problem structure:
    # t consists of '+' and '-' only
    # s consists of '+', '-', and '?'
    # Here, we let t have roughly half '+' and half '-'
    # and s have the same first part as t and the rest as '?' so that
    # n directly controls the size of s.

    if n <= 0:
        print("0.0")
        return

    # Build t: first n//2 are '+', rest are '-'
    half = n // 2
    t = "+" * half + "-" * (n - half)

    # Build s: first n//3 same as t's prefix, remaining are '?'
    prefix_len = n // 3
    s_prefix = t[:prefix_len]
    s = s_prefix + "?" * (n - prefix_len)

    k = t.count('+') - s.count('+')
    q = s.count('?')

    if k > q or k < 0:
        print('0.0')
    else:
        # C(q, k) / 2^q
        res = math.factorial(q) / (math.factorial(k) * math.factorial(q - k)) / (2 ** q)
        # Match original printing style
        print(res)


if __name__ == "__main__":
    # Example deterministic call
    main(10)