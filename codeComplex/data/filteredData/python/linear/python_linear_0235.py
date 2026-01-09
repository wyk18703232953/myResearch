def main(n):
    # Generate a deterministic string of length n over 'x' and 'y'
    # Pattern: positions where i % 3 == 0 or 1 are 'x', others are 'y'
    string = ''.join('x' if i % 3 in (0, 1) else 'y' for i in range(n))

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

    # print(total)
    pass
if __name__ == "__main__":
    main(1000)