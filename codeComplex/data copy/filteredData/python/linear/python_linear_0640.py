def main(n):
    # Ensure n is non-negative
    if n < 0:
        return

    # Deterministically generate T based on n
    # Example pattern: mix of values <2 and >=2, all derived from n and index
    # This keeps structure similar to possible original inputs while being deterministic.
    T = []
    for i in range(n):
        # Generate values in [0, 5] deterministically
        val = (i * 3 + n) % 6
        T.append(val)

    # Original logic starts here
    L = []
    M = []
    t = 0
    ip = 0
    IP = []
    for i in range(n):
        if T[i] >= 2:
            L.append(i + 1)
            M.append(T[i])
            t += T[i]

        else:
            ip += 1
            IP.append(i + 1)
    if t - (2 * len(L) - 2) < ip:
        # print("NO")
        pass

    else:
        for i in range(1, len(L) - 1):
            M[i] -= 2
        if len(L) >= 2:
            M[0] -= 1
            M[-1] -= 1
        # print("YES", end=' ')
        pass

        if ip == 0:
            # print(len(L) - 1)
            pass
        elif ip == 1:
            # print(len(L))
            pass

        else:
            # print(len(L) + 1)
            pass
        # print(len(L) - 1 + ip)
        pass

        if ip >= 1:
            # print(IP[0], end=' ')
            pass
            # print(L[0])
            pass
            M[0] -= 1
        if ip >= 2:
            # print(IP[-1], end=' ')
            pass
            # print(L[-1])
            pass
            M[-1] -= 1
        k = 1
        ind = 0
        while k < ip - 1:
            if M[ind] == 0:
                ind += 1

            else:
                # print(IP[k], end=' ')
                pass
                # print(L[ind])
                pass
                M[ind] -= 1
                k += 1
        for i in range(len(L) - 1):
            # print(L[i], end=' ')
            pass
            # print(L[i + 1])
            pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)