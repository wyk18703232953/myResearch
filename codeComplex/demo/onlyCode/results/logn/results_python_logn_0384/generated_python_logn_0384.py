def main(n):
    import sys
    assert n >= 2 and n % 2 == 0
    arr = [i for i in range(n // 2)] * 2

    def ask(i):
        return arr[i]

    def answer(i):
        return i + 1 if i != -1 else -1

    def has_intersection(l1, r1, l2, r2):
        if l1 <= l2 and r2 <= r1:
            return True
        if l2 <= l1 and r1 <= r2:
            return True
        return False

    if (n // 2) % 2 == 1:
        return answer(-1)
    else:
        assert n % 4 == 0
        l1 = 0
        r1 = n // 2
        a_l1 = ask(l1)
        a_r1 = ask(r1)
        if a_l1 == a_r1:
            return answer(0)
        a_l2 = a_r1
        a_r2 = a_l1
        while True:
            m1 = (l1 + r1) // 2
            m2 = (m1 + n // 2) % n
            a_m1 = ask(m1)
            a_m2 = ask(m2)
            if a_m1 == a_m2:
                return answer(m1)
            if has_intersection(a_l1, a_m1, a_l2, a_m2):
                r1 = m1
                a_r1 = a_m1
                a_r2 = a_m2
            else:
                assert has_intersection(a_m1, a_r1, a_m2, a_r2)
                l1 = m1
                a_l1 = a_m1
                a_l2 = a_m2

if __name__ == "__main__":
    print(main(8))