def main(n):
    # n controls the number of digits of a; b is fixed to keep behavior deterministic and scalable
    if n <= 0:
        return ""
    # construct a as a deterministic n-digit number using a simple pattern
    # e.g., for n=5 -> digits "12345", for n=12 -> "123456789012"
    digits = [(i % 10) for i in range(1, n + 1)]
    a = int("".join(str(d) for d in digits))
    # choose b as a deterministic function of n; ensure it's large enough to allow permutations
    # here we choose b = a * 2, which monotonically grows with n
    b = a * 2

    arr = list(str(a))
    arr = sorted(arr)
    ans = ""

    # core logic copied from original program, but using our generated a, b
    while arr:
        for i in range(len(arr) - 1, -1, -1):
            x = ans + arr[i]
            for j in arr[:i]:
                x += j
            for j in arr[i + 1:]:
                x += j
            if int(x) <= b:
                ans += arr[i]
                arr.pop(i)
                break

    # for experimental use we both return and print the result
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # example deterministic run for time-complexity experiments
    main(10)