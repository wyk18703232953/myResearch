def main(n):
    # Deterministically generate s based on n
    # Example pattern: alternate '+' and '-', length n
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    # Original logic starts here, using generated n and s
    for i in range(n + 1):
        flag = True
        stones = i
        for j in s:
            if j == '-':
                if stones > 0:
                    stones -= 1

                else:
                    flag = False
                    break

            else:
                stones += 1

        if flag:
            n = i
            break

    stones = n
    for i in s:
        if i == '-':
            stones -= 1

        else:
            stones += 1

    # print(stones)
    pass
if __name__ == "__main__":
    main(10)