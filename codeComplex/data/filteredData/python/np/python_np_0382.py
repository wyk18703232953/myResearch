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
        for d in trace.get(trace_mask):
            fr, to, v = d
            res[fr] = (v, to)
        return

    sub_mask = back[trace_mask]
    build_mask(sub_mask)
    build_mask(trace_mask - sub_mask)


def main(n):
    global data, position, nxt, agg_sum, trace, F, back, total_sum, res
    data = defaultdict(list)
    position = defaultdict()
    nxt = defaultdict()
    agg_sum = list()
    trace = defaultdict()
    total_sum = 0

    k = max(1, n)

    F = [False for _ in range(1 << k)]
    back = [0 for _ in range(1 << k)]
    res = [(0, 0) for _ in range(k)]

    # Deterministic data generation:
    # For each row i, generate k values: v = i * k + j + 1
    # This makes total_sum = k * sum(row[i]) and guarantees divisibility by k
    for i in range(k):
        values = [k] + [i * k + j + 1 for j in range(k)]
        row_vals = values[1:]
        data[i] = row_vals

        agg_sum.append(sum(row_vals))
        total_sum += agg_sum[i]

        for cnt, v in enumerate(row_vals, 0):
            position[v] = (i, cnt)

    if total_sum % k != 0:
        # For this deterministic generator, this should not happen
        return "No"

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
        build_mask((1 << k) - 1)
        # Return result instead of printing to keep it suitable for experiments
        return "Yes", [(value[0], value[1] + 1) for value in res]
    else:
        return "No"


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    out = main(3)
    if isinstance(out, str):
        print(out)
    else:
        print(out[0])
        for v in out[1]:
            print(v[0], v[1])