def main(n):
    # Deterministic generation of a, b
    a = n % 7 + 1
    b = (n % 5) + 2

    # Deterministic generation of ghosts: list of (vx, vy)
    # Use simple arithmetic patterns based on i and n
    ghosts = []
    for i in range(n):
        vx = (i * 2 + 1) % (n + 3)
        vy = (i * 3 + 2) % (n + 5)
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
    main(1000)