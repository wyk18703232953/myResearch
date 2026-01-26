def main(n):
    # Deterministically generate input strings a_str and b_str of length n
    # Digits are in [0..9] using modular arithmetic
    a_str = ''.join(str((i * 3 + 1) % 10) for i in range(n))
    b_str = ''.join(str((i * 7 + 2) % 10) for i in range(n))

    # Core logic from original program
    a = sorted(map(int, a_str))
    b = list(map(int, b_str))
    bn = int(''.join(map(str, b)))
    res = int(''.join(map(str, sorted(a))))
    if len(b) != len(a):
        # print(''.join(map(str, sorted(a, reverse=True))))
        pass

    else:
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] < a[j] < b[i]:
                    a[i], a[j] = a[j], a[i]
            tmp = int(''.join(map(str, a[:i + 1] + sorted(a[i + 1:], reverse=True))))
            res = max(res, tmp) if tmp <= bn else res
            for j in range(i + 1, len(a)):
                if a[j] == b[i]:
                    a[i], a[j] = a[j], a[i]
        # print(res)
        pass
if __name__ == "__main__":
    main(10)