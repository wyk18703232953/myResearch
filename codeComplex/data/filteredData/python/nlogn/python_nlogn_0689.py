def main(n):
    # Map n to sizes of the two lists
    # Ensure both lists are non-empty and reasonably large for scaling
    a = max(1, n // 2)
    b = max(1, n - a)

    # Deterministically generate l1 and l2 based on n
    # l1: ascending sequence starting from 1
    l1 = [i + 1 for i in range(a)]
    # l2: sequence depending on n to vary structure
    l2 = [(i * 2 + (n % 5)) for i in range(b)]

    n = len(l1)
    m = len(l2)

    l1.sort()
    l2.sort()
    l2 = l2[::-1]

    if n == 1:
        if l1[0] != min(l2):
            # print(-1)
            pass

        else:
            # print(sum(l2))
            pass
    elif max(l1) > min(l2):
        # print(-1)
        pass

    else:
        l1 = l1[::-1]
        if min(l2) == l1[0]:
            # print(sum(l2) + (sum(l1) - l1[0]) * m)
            pass

        else:
            # print(sum(l2) + l1[0] + sum(l1[1:]) * m - l1[1])
            pass
if __name__ == "__main__":
    main(10)