from collections import defaultdict

data = defaultdict(list)
position = defaultdict()
nxt = defaultdict()
agg_sum = list()

trace = defaultdict()
F = []
back = []
total_sum = 0
res = []


def build_mask(trace_mask):
    if trace_mask == 0:
        return

    if trace.get(trace_mask):
        for item in trace.get(trace_mask):
            fr, to, v = item
            res[fr] = (v, to)
        return

    sub_mask = back[trace_mask]
    build_mask(sub_mask)
    build_mask(trace_mask - sub_mask)


def generate_input(n):
    # Interpret n as k (number of rows / groups)
    k = max(1, n)

    rows = []
    # Deterministic construction of values:
    # row i has i+1 elements, value formula: i * (k + 1) + j
    # First number in each row is the count, followed by the values.
    for i in range(k):
        length = i + 1
        row_values = [length]
        for j in range(length):
            v = i * (k + 1) + j
            row_values.append(v)
        rows.append(row_values)

    return k, rows


def main(n):
    global data, position, nxt, agg_sum, trace, F, back, total_sum, res

    # Reinitialize global state for repeatability across multiple calls
    data = defaultdict(list)
    position = defaultdict()
    nxt = defaultdict()
    agg_sum = []
    trace = defaultdict()
    total_sum = 0

    k, rows = generate_input(n)

    F = [False for _ in range(1 << k)]
    back = [0 for _ in range(1 << k)]
    res = [(0, 0) for _ in range(k)]

    # Simulate the original input reading using deterministic rows
    for i in range(k):
        values = rows[i]
        data[i] = values[1:]

        agg_sum.append(sum(data[i]))
        total_sum += agg_sum[i]

        for cnt, v in enumerate(data[i], 0):
            position[v] = (i, cnt)

    if total_sum % k != 0:
        print("No")
        return

    row_sum = total_sum // k

    for i in range(k):
        for cnt, value in enumerate(data.get(i), 0):

            x = i
            y = cnt
            mask = (1 << x)
            could = True
            circle = list()
            while True:
                next_value = row_sum - agg_sum[x] + data.get(x)[y]
                if position.get(next_value) is None:
                    could = False
                    break

                last_x = x
                last_y = y

                x, y = position.get(next_value)
                circle.append((x, last_x, next_value))

                if x == i and y == cnt:
                    break

                if mask & (1 << x):
                    could = False
                    break

                mask |= (1 << x)

            F[mask] |= could
            if could:
                trace[mask] = circle

    for mask in range(1, 1 << k):
        sub = mask
        while sub > 0:
            if F[sub] and F[mask - sub]:
                F[mask] = True
                back[mask] = sub
                break
            sub = mask & (sub - 1)

    if F[(1 << k) - 1]:
        print('Yes')
        build_mask((1 << k) - 1)
        for value in res:
            print(value[0], value[1] + 1)
    else:
        print('No')


if __name__ == "__main__":
    # Example deterministic run; change n as needed for experiments
    main(4)