def lvl(val):
    tot = 1
    curr = -1
    while val % tot == 0:
        curr += 1
        tot *= 2
    return [curr, val * 2 // tot, tot // 2]


def main(n):
    # Interpret n as total nodes; derive a deterministic number of queries
    # For scalability, let q grow with n but not exceed n
    if n <= 0:
        return
    q = max(1, n // 2)

    results = []
    for i in range(1, q + 1):
        # Deterministic starting position in [1, n]
        curr = (i * 3 % n) + 1

        # Deterministic command string length based on i and n
        length = (i * 5) % 20 + 1

        # Build deterministic command string using a pattern over "URL"
        cmds = []
        for k in range(length):
            r = (i + k) % 3
            if r == 0:
                cmds.append("U")
            elif r == 1:
                cmds.append("R")
            else:
                cmds.append("L")
        s = "".join(cmds)

        l, v, pw = lvl(curr)
        for j in s:
            if j == "U":
                if v % 4 == 3:
                    curr = curr - pw
                else:
                    if curr + pw <= n:
                        curr = curr + pw
            elif j == "R":
                if l > 0:
                    curr = curr + pw // 2
            elif j == "L":
                if l > 0:
                    curr = curr - pw // 2
            l, v, pw = lvl(curr)

        results.append(curr)

    for x in results:
        print(x)


if __name__ == "__main__":
    main(16)