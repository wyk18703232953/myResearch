def main(n):
    # n controls the total number of positions (n taxis + m passengers = n)
    if n <= 1:
        # Degenerate case: no passengers or no taxis
        # print(0)
        pass
        return

    total = n

    # Deterministic split of total into n_taxis and m_passengers
    n_taxis = total // 2
    m_passengers = total - n_taxis

    # Generate xs as distinct positions: 0, 1, 2, ..., total-1
    xs = list(range(total))

    # Generate ts: first n_taxis as taxis (1), remaining as passengers (0)
    ts = [1] * n_taxis + [0] * m_passengers

    taxi_idx = sorted([xs[idx] for idx in range(n_taxis + m_passengers) if ts[idx] == 1])
    passenger_idx = sorted([xs[idx] for idx in range(n_taxis + m_passengers) if ts[idx] == 0])

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
    main(10)