import random

#------------------------original logic (slightly refactored)-------------------#

def ok(a, b, c):
    n = a[0][-1]
    ans = []
    for _ in range(a[0][0]):
        ans.append([a[1]] * n)

    l = n
    r = n - a[0][0]

    for i in range(2):
        for j in range(2):
            l1, r1 = b[0]
            l2, r2 = c[0]

            if i:
                l1, r1 = r1, l1
            if j:
                l2, r2 = r2, l2

            if l1 == l:
                if l2 != l or r1 + r2 != r:
                    continue
                for _ in range(r1):
                    ans.append([b[1]] * n)
                for _ in range(r2):
                    ans.append([c[1]] * n)
                return ans

            if l1 == r:
                if l2 != r or r1 + r2 != l:
                    continue
                for _ in range(r):
                    ans.append([b[1]] * r1 + [c[1]] * r2)
                return ans

    return False


#------------------------test-data + main(n)------------------------------------#

def main(n):
    """
    n: positive integer controlling the scale of generated test data.
    We generate three segments [l1,r1], [l2,r2], [l3,r3].
    Each segment length is in [1, n], and l <= r.
    """

    if n <= 0:
        print(-1)
        return

    # Generate lengths in [1, n]
    len1 = random.randint(1, n)
    len2 = random.randint(1, n)
    len3 = random.randint(1, n)

    # Place them on a conceptual line starting at 1 so l <= r holds
    # and they don't overlap (just for structured data, not required by logic)
    l1 = 1
    r1 = l1 + len1 - 1
    l2 = r1 + 1
    r2 = l2 + len2 - 1
    l3 = r2 + 1
    r3 = l3 + len3 - 1

    a = [sorted((l1, r1)), 'A']
    b = [sorted((l2, r2)), 'B']
    c = [sorted((l3, r3)), 'C']

    A = ok(a, b, c)
    B = ok(b, a, c)
    C = ok(c, a, b)

    if A:
        print(len(A))
        for row in A:
            print(*row, sep="")
    elif B:
        print(len(B))
        for row in B:
            print(*row, sep="")
    elif C:
        print(len(C))
        for row in C:
            print(*row, sep="")
    else:
        print(-1)


if __name__ == "__main__":
    # Example: run with scale n = 10
    main(10)