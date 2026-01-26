def solve(n, k, t):
    j = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            j = i
    s = t + (k - 1) * t[-(n - j):]
    return s

def main(n):
    if n <= 0:
        return ""
    k = n
    base_chars = "abc"
    t = "".join(base_chars[i % len(base_chars)] for i in range(n))
    result = solve(n, k, t)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(5)