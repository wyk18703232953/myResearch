def main(n):
    # Interpret n as the number of elements in the sequence
    # Deterministically generate n integers with possible duplicates
    # Example pattern: a[i] = (i * 2) // 3 - 5
    a = [(i * 2) // 3 - 5 for i in range(n)]

    a = sorted(set(a))

    if len(a) > 1:
        x = iter(a)
        next(x)
        print(next(x))
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)