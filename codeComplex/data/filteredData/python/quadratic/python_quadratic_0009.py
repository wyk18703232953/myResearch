def main(n):
    import math

    # Deterministic data generation
    # radius fixed, x_list constructed deterministically from n
    radii = 5
    x_list = [(i * 3) % (4 * radii) for i in range(n)]

    temp_arr = []
    for i in range(n):
        candidates = [radii]
        for j in range(i):
            dx = x_list[i] - x_list[j]
            if abs(dx) <= 2 * radii:
                val = math.sqrt(4 * radii ** 2 - dx ** 2) + temp_arr[j]
                candidates.append(val)
        temp_arr.append(max(candidates))

    for v in temp_arr:
        # print(v, end=" ")
        pass
if __name__ == "__main__":
    main(10)