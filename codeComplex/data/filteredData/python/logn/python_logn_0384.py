def main(n):
    # n must be even and divisible by 4 to follow original logic
    if n < 2 or n % 2 != 0:
        return -1

    # Deterministic construction of array a of size n
    # We need a[i] and a[i + n//2] such that solution exists for n % 4 == 0
    # Construct piecewise linear so that a[0] != a[n//2] but there is some i with a[i] == a[i + n//2]
    a = [0] * n
    half = n // 2
    # First half: strictly increasing
    for i in range(half):
        a[i] = i
    # Second half: mirror first half but shifted so that somewhere equals
    # For i in [half//2, half), we will have a[i] == a[i-half]
    shift = half // 2
    for i in range(half):
        a[half + i] = (i + shift) % half

    def ask(i):
        return a[i]

    def has_intersection(l1, r1, l2, r2):
        if l1 <= l2 and r2 <= r1:
            return True
        if l2 <= l1 and r1 <= r2:
            return True
        return False

    if (n // 2) % 2 == 1:
        return -1

    else:
        l1 = 0
        r1 = n // 2
        a_l1 = ask(l1)
        a_r1 = ask(r1)
        if a_l1 == a_r1:
            return 0
        a_l2 = a_r1
        a_r2 = a_l1
        while True:
            m1 = (l1 + r1) // 2
            m2 = (m1 + n // 2) % n
            a_m1 = ask(m1)
            a_m2 = ask(m2)
            if a_m1 == a_m2:
                return m1
            if has_intersection(a_l1, a_m1, a_l2, a_m2):
                r1 = m1
                a_r1 = a_m1
                a_r2 = a_m2

            else:
                l1 = m1
                a_l1 = a_m1
                a_l2 = a_m2


if __name__ == "__main__":
    # example call for time complexity experiments
    result = main(16)
    # print(result)
    pass