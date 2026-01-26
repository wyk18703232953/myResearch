def main(n):
    # n controls the number of digits of a and (roughly) the number of digits of b
    # Ensure at least 1 digit
    if n <= 0:
        n = 1

    # Deterministically construct a n‑digit number a using digits cycling 1..9 then 0
    digits_a = [(i % 10) for i in range(1, n + 1)]
    # Avoid leading zero: if the first digit becomes 0, set it to 1
    if digits_a[0] == 0:
        digits_a[0] = 1
    a = 0
    for d in digits_a:
        a = a * 10 + d

    # Deterministically construct b based on n so that scale is comparable to a
    # Here: b is a number with n digits, each digit = (n % 10)
    digit_b = n % 10
    if digit_b == 0:
        digit_b = 9
    b = 0
    for _ in range(n):
        b = b * 10 + digit_b

    # Core algorithm from original program: build maximum string ans from digits of a
    # such that the resulting number <= b
    c = sorted(list(str(a)))
    ans = ""

    while c:
        for i in range(len(c) - 1, -1, -1):
            candidate_list = list(ans) + [c[i]] + c[:i] + c[i + 1:]
            candidate = int("".join(candidate_list))
            if candidate <= b:
                ans += c[i]
                c.pop(i)
                break

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # Example deterministic calls for time‑complexity experiments
    for size in (1, 2, 3, 5, 10):
        main(size)