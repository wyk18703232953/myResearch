def main(n):
    import bisect

    # Interpret n as both number of warriors and number of queries
    warriors = n
    queries = n

    # Deterministically generate strengths: strength[i] = i+1
    strength = [i + 1 for i in range(warriors)]

    # Deterministically generate arrows: arrows[i] = (i % warriors) + 1
    arrows = [(i % warriors) + 1 for i in range(queries)]

    # Original logic
    for i in range(1, warriors):
        strength[i] += strength[i - 1]

    No_arrows = 0
    warriors_minus_one = warriors - 1

    for i in range(queries):
        No_arrows += arrows[i]
        if No_arrows >= strength[-1]:
            No_arrows = 0
            print(warriors_minus_one + 1)
        else:
            it = bisect.bisect_left(strength, No_arrows)
            if strength[it] == No_arrows:
                print(warriors_minus_one - it + 1)
            else:
                print(warriors_minus_one - it + 2)


if __name__ == "__main__":
    main(10)