import math

def generate_input(n):
    # n controls both number of disks and radius in a deterministic way
    # ensure at least 1 disk and radius >= 1
    num_disks = max(1, n)
    r = max(1, n // 2 + 1)
    # deterministic x coordinates: spaced by r to allow overlaps for small r
    x_cord = [i * r for i in range(num_disks)]
    return num_disks, r, x_cord

def core_logic(n, r, x_cord):
    y_cord = []
    for i, x in enumerate(x_cord):
        if len(y_cord) == 0:
            y_cord.append(r)

        else:
            y_cord.append(r)
            for j in range(i):
                diff = abs(x_cord[i] - x_cord[j])
                if diff <= 2 * r:
                    y_cord[i] = max(y_cord[i], math.sqrt(4 * r * r - diff ** 2) + y_cord[j])
    return y_cord

def main(n):
    n_disks, r, x_cord = generate_input(n)
    y_cord = core_logic(n_disks, r, x_cord)
    # print(" ".join(str(v) for v in y_cord))
    pass
if __name__ == "__main__":
    main(10)