def main(n):
    # Ensure n is at least 1 to avoid empty string edge cases
    if n <= 0:
        print(0)
        return

    # Deterministically generate a string of length n
    # Pattern: positions where (i % 4 in {0,1,2}) are 'x', others are 'y'
    # This guarantees frequent runs of 'x' of length 3
    string = ''.join('x' if (i % 4 in (0, 1, 2)) else 'y' for i in range(n))

    i = 0
    j = 0
    total = 0

    while j < len(string):
        flag = False
        count = 0
        while j < len(string) and string[i] == 'x' and string[j] == 'x':
            count += 1
            flag = True
            j += 1

        if count >= 3:
            total += (count - 3) + 1
        if flag:
            i = j
        else:
            i += 1
            j += 1

    print(total)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(20)