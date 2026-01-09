def main(n):
    # Interpret n as the interval length j = r - l + 1
    # Deterministically choose l = 1, so r = n
    l = 1
    r = n
    j = r - l + 1

    if j == 3:
        if l % 2 == 0:
            # print(l, l + 1, l + 2)
            pass

        else:
            # print(-1)
            pass
    elif j > 3:
        if l % 2 == 0:
            # print(l, l + 1, l + 2)
            pass

        else:
            # print(l + 1, l + 2, l + 3)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)