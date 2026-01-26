def main(n):
    # Interpret n as number of circles; radius fixed as in typical CF constraints
    r = 1
    if n <= 0:
        # print()
        pass
        return

    # Deterministic x-coordinates: evenly spaced by r (can overlap in influence)
    x = [i * r for i in range(n)]

    y = []
    for xi in x:
        yi = float(r)
        for tx, ty in zip(x, y):
            if xi - 2 * r <= tx <= xi + 2 * r:
                dy = (4.0 * r ** 2 - (tx - xi) ** 2) ** 0.5
                yi = max(yi, ty + dy)
        y.append(yi)
    # print(*y)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(5)