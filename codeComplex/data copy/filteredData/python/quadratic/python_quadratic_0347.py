def main(n):
    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Deterministically generate first and second strings of length n
    # Use a simple periodic pattern over lowercase letters
    first = [chr(ord('a') + (i % 26)) for i in range(n)]
    # second is a shifted version of first to keep the transformation non-trivial
    shift = 3
    second = [chr(ord('a') + ((i + shift) % 26)) for i in range(n)]

    swap = []
    can = True

    for i in range(n):
        if first[i] != second[i]:
            cont = -1
            for j in range(i, n):
                if first[j] == second[i]:
                    cont = j
                    break

            if cont != -1:
                for j in range(cont, i, -1):
                    first[j], first[j - 1] = first[j - 1], first[j]
                    swap.append(j)

            else:
                can = False

    if can:
        # print(len(swap))
        pass

        if swap:
            # print(*swap, end=' ')
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example call; you can change n for different scales
    main(10)