def main(n):
    # Interpret n as total number of positions (n+m in original code)
    # Ensure at least 2 positions to have both taxis and passengers
    total = max(2, n)

    # Deterministically split into n (passengers) and m (taxis)
    # Let about half be taxis, half passengers, with at least 1 taxi and 1 passenger
    m = max(1, total // 2)
    n_passengers = total - m
    if n_passengers == 0:
        n_passengers = 1
        m = total - 1

    # Generate positions xs deterministically: 0, 1, 2, ..., total-1
    xs = [i for i in range(total)]

    # Generate ts deterministically:
    # First n_passengers as passengers (0), next m as taxis (1)
    ts = [0] * n_passengers + [1] * m

    # Core logic from original program
    taxi_idx = sorted([xs[idx] for idx in range(total) if ts[idx] == 1])
    passenger_idx = sorted([xs[idx] for idx in range(total) if ts[idx] == 0])

    a_is = [0] * len(taxi_idx)
    t_idx = 0
    p_idx = 0

    while True:
        if p_idx >= len(passenger_idx):
            break

        if t_idx == len(taxi_idx) - 1:
            a_is[t_idx] += 1

        else:
            while t_idx < len(taxi_idx) - 1:
                d1 = abs(passenger_idx[p_idx] - taxi_idx[t_idx])
                d2 = abs(passenger_idx[p_idx] - taxi_idx[t_idx + 1])
                if d1 > d2:
                    t_idx += 1

                else:
                    break

            a_is[t_idx] += 1

        p_idx += 1

    # print(' '.join(str(x) for x in a_is))
    pass
if __name__ == "__main__":
    # Example deterministic call for testing / timing
    main(10)