def main(n):
    # In this refactored version, we simulate the interactive judge deterministically.
    # For a given n, we choose a pair (A, B) whose bit-length is O(n).
    # The original algorithm assumes up to 30 bits, so we cap at 30 bits.
    max_bits = 30
    bits = min(max_bits, max(1, n))

    # Deterministically construct A and B from n.
    # Make sure A != B for most n to exercise the general branch; for a specific n (e.g., n == 1),
    # we can use A == B to exercise the equal branch.
    if n == 1:
        A = 0
        B = 0

    else:
        # Simple deterministic pattern based on n
        A = 0
        B = 0
        for i in range(bits):
            if i % 2 == 0:
                A |= (1 << i)
            if i % 3 == 0:
                B |= (1 << i)

        # Ensure A != B for n > 1
        if A == B:
            B ^= 1

    def judge(c, d):
        # Simulates the interactive response:
        # returns -1 if A < B, 1 if A > B, 0 if A == B
        if A < B:
            return -1
        elif A > B:
            return 1

        else:
            return 0

    def solve():
        c, d = 0, 0
        ans = judge(c, d)
        if ans == 0:
            # both the numbers are equal
            num = 0
            for i in range(29, -1, -1):
                c_local = 1 << i
                d_local = 0
                ans_local = judge(c_local, d_local)
                if ans_local == 0:
                    # A == B and both equal, so no informative response here; just follow original logic:
                    # In the original interactive problem, this branch wouldn't generally be reachable
                    # with A == B, but we keep structure.
                    continue
                if ans_local == -1:
                    num += (1 << i)
            # print(num, num)
            pass

        else:
            l = [0, 0]
            if ans == 1:
                cur = 0

            else:
                cur = 1

            prev = ans
            c_local, d_local = c, d
            # first find set of mutually exclusive bits
            for i in range(29, -1, -1):
                tc = c_local | (1 << i)
                td = d_local | (1 << i)
                ans_local = judge(tc, td)
                if ans_local == 0:
                    break
                if ans_local != prev:
                    l[cur] += (1 << i)
                    if cur == 0:
                        c_local = tc

                    else:
                        d_local = td
                    temp = judge(c_local, d_local)
                    prev = temp
                    if temp == 1:
                        cur = 0

                    else:
                        cur = 1
            c_local = l[0]
            d_local = l[1]
            # now try to find common bits
            for i in range(29, -1, -1):
                if (c_local & (1 << i)) != 0 or (d_local & (1 << i)) != 0:
                    continue
                tc = c_local | (1 << i)
                ans_local = judge(tc, d_local)
                if ans_local == -1:
                    l[0] |= (1 << i)
                    l[1] |= (1 << i)
            # print(l[0], l[1])
            pass

    solve()


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)