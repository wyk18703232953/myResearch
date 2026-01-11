def next_index(k, a, x):
    while k < len(a) and a[k] < x:
        k += 1
    return k

def core_algorithm(n, m, vert, horz_all):
    horz = []
    for x1, x2, y in horz_all:
        if x1 == 1:
            horz.append(x2)

    vert.sort()
    horz.sort()

    vert.append(1000000000)

    num = next_index(0, horz, vert[0])

    ans = len(horz) - num

    for i in range(1, len(vert)):
        num2 = next_index(num, horz, vert[i])
        t = i + len(horz) - num2
        if t < ans:
            ans = t
        num = num2

    return ans

def generate_data(n):
    # Interpret n as both number of vertical lines and number of horizontal segments
    # Deterministic generation:
    # vert[i] = i * 2 + 1
    # horiz segments: alternate x1 between 0 and 1, x2 increasing, y = fixed or derived
    num_vert = n
    num_horz = n

    vert = [i * 2 + 1 for i in range(num_vert)]

    horz_all = []
    for i in range(num_horz):
        x1 = 1 if i % 2 == 0 else 0
        x2 = i * 3 + 2
        y = i  # y is irrelevant for the algorithm, but keep deterministic
        horz_all.append((x1, x2, y))

    return num_vert, num_horz, vert, horz_all

def main(n):
    n_vert, n_horz, vert, horz_all = generate_data(n)
    result = core_algorithm(n_vert, n_horz, vert, horz_all)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)