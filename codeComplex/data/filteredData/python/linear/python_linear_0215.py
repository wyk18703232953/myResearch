def main(n):
    # n: number of ghosts / lines of data
    # Deterministic generation of a, b and ghosts
    # a and b are simple functions of n to keep variety while deterministic
    a = n % 7 + 1
    b = (n // 3) % 5 + 1

    # Generate n tuples (vx, vy) deterministically from n, a, b
    ghosts = []
    for i in range(1, n + 1):
        vx = (i * a + b) % (2 * n + 3)
        vy = (i * b + a) % (3 * n + 5)
        ghosts.append((vx, vy))

    speeds = {}
    for vx, vy in ghosts:
        vl = a * vx - vy
        k = vx + a * vy
        ss = speeds.setdefault(vl, {})
        ss[k] = ss.get(k, 0) + 1

    result = 0
    for vl, ss in speeds.items():
        group_size = sum(ss.values())
        for sss in ss.values():
            result += sss * (group_size - sss)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)