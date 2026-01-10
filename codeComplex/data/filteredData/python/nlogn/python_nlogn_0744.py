def main(n):
    # Interpret n as the size N of the array A
    N = max(1, n)

    # Deterministically generate A of size N
    # Pattern: A[i] = i // 2  (creates duplicates, increasing values)
    A = [i // 2 for i in range(N)]

    A.sort()
    duplicates = 0
    i = 1
    temp = 1
    ind = -1
    while i < N:
        temp = 1
        while i < N and A[i] == A[i - 1]:
            ind = i - 1
            temp += 1
            i += 1
        i += 1

        if temp != 1:
            duplicates += 1
        if temp > 2:
            break

    turns = sum(A) - N * (N - 1) // 2

    if temp > 2 or duplicates > 1:
        print('cslnb')
    else:
        output = 'cslnb'
        if duplicates == 0:
            if turns % 2 == 1:
                output = 'sjfnb'
        else:
            if ind - 1 >= 0:
                if A[ind - 1] == A[ind] - 1:
                    output = 'cslnb'
                else:
                    if turns % 2 == 1:
                        output = 'sjfnb'
            else:
                if A[ind] == 0:
                    output = 'cslnb'
                else:
                    if turns % 2 == 1:
                        output = 'sjfnb'
        print(output)


if __name__ == "__main__":
    main(10)