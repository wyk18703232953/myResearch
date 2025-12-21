def main(n):
    import random
    import string
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    o = len(s)
    k = 0
    for i in range(o):
        r = {0}
        for j in range(o - i + 1):
            if s[j:j + i] in r:
                k = max(i, k)
            else:
                r.add(s[j:j + i])
    return k

if __name__ == "__main__":
    print(main(10))