def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def core_algorithm(s_list):
    n = len(s_list)
    cnt = 0
    sm = 0
    s = [int(ch) % 3 for ch in s_list]
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
    return cnt


def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate a digit string of length n
    # Pattern: digits cycle through '0'..'9'
    s = [str(i % 10) for i in range(n)]

    result = core_algorithm(s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)