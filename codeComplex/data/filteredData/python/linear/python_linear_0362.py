import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(n):
    s = []
    for i in range(n):
        s.append((i * 7 + 3) % 10)
    cnt = 0
    sm = 0
    for i in range(n):
        s[i] = int(s[i]) % 3
    i = 0
    while i < n:
        if s[i] == 0:
            cnt += 1
            sm = 0
            i += 1

        else:
            sm += s[i]
            if sm % 3 == 0:
                sm = 0
                cnt += 1
                i += 1

            else:
                if i + 1 < n and s[i] + s[i + 1] == 3:
                    i += 2
                    cnt += 1
                    sm = 0

                else:
                    i += 1
    # print(cnt)
    pass
if __name__ == "__main__":
    main(100000)