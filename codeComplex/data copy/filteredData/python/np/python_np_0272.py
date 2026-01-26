def main(n):
    # Interpret n as:
    # n: original n (tree size scale)
    # q: number of queries, set equal to n
    # ui: i for i in range(1, q+1)
    # si: deterministic pattern based on i and n
    n_val = max(1, n)
    q = n_val

    # Original precomputation of par
    par = n_val // 2 + 1
    par = len(list(bin(par)[2:]))

    results = []

    for idx in range(q):
        # Deterministic ui: from 1 to q
        ui = idx + 1

        # Deterministic si:
        # pattern length cycles with par, characters depend on ui and index
        length = par + (ui % par)
        chars = []
        for j in range(length):
            r = (ui + j) % 3
            if r == 0:
                chars.append("U")
            elif r == 1:
                chars.append("L")
            else:
                chars.append("R")
        si = "".join(chars)

        temp = bin(ui)[2:]
        now = len(temp)
        num = list((par - now) * "0" + temp)
        now = par - now

        for i in range(len(num)):
            if str(num[i]) == '1':
                now = i

        for ch in si:
            if ch == "U":
                if now == 0:
                    continue
                num[now] = 0
                now -= 1
                num[now] = 1
            elif ch == "L":
                if str(num[-1]) == '1':
                    continue
                num[now] = 0
                now += 1
                num[now] = 1
            else:
                if str(num[-1]) == '1':
                    continue
                now += 1
                num[now] = 1

        for i in range(par):
            num[i] = str(num[i])
        result = int("".join(num), 2)
        results.append(result)

    # For experimental runs, print all outputs to preserve behavior
    for x in results:
        print(x)


if __name__ == "__main__":
    # Example call for experimentation; change n as needed
    main(10)