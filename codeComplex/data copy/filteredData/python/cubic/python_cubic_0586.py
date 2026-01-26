def main(n):
    # deterministic input generation from n
    digits = [str((i % 10)) for i in range(max(1, n))]
    a = digits[:]  # list of digit characters
    b = int("".join(digits)) if digits else 0

    a.sort(reverse=True)
    ans = ''
    while len(a) > 0:
        for i in range(len(a)):
            tmp = ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(tmp) <= b:
                ans += a[i]
                a = a[:i] + a[i + 1:]
                break

        else:
            break
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)