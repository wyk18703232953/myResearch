def main(n):
    # Deterministically generate input list l of length n
    # Original code assumes at least 1 element
    if n <= 0:
        return

    # Example deterministic construction:
    # l[i] = i // 2  (creates some duplicates and structure)
    l = [i // 2 for i in range(n)]
    l.sort()

    def f(l, n):
        dou = False
        for k in range(1, n):
            if l[k] == l[k - 1]:
                if (
                    dou
                    or l[k] == 0
                    or (k >= 2 and l[k] == l[k - 2] and n != 2)
                    or (k >= 2 and l[k] == l[k - 2] + 1)
                ):
                    return False
                else:
                    dou = True
        return (sum(l) - (n * (n - 1)) // 2) % 2

    if f(l, n):
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)