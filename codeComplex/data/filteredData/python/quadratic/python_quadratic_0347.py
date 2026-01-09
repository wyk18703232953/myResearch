def main(n):
    if n <= 0:
        # print(-1)
        pass
        return

    # Deterministic generation of first and second strings of length n
    # first: repeating pattern 'a','b','c',...
    first = [chr(ord('a') + (i % 26)) for i in range(n)]
    # second: right-rotated version of first
    second = first[-1:] + first[:-1] if n > 1 else first[:]

    first = list(first)
    second = list(second)

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
                break

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
    main(10)