def main(n):
    # Generate deterministic input of length 14 based on n
    # Example: values depend on n and index, but are fully deterministic
    a = [((n + i * 3) % 50) for i in range(14)]

    h = 0
    for i_outer in range(14):
        b = a[:]
        if i_outer == 13:
            j = 0

        else:
            j = i_outer + 1
        if a[i_outer] > 0:
            c = 0
            t = b[i_outer] % 14
            x = b[i_outer] // 14
            b[i_outer] = 0
            for k in range(14):
                b[k] += x
            while t > 0:
                b[j] += 1
                j += 1
                if j == 14:
                    j = 0
                t -= 1
            for k in range(14):
                if b[k] % 2 == 0:
                    c += b[k]
            if c > h:
                h = c
    # print(h)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(1000)