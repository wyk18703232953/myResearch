def main(n):
    # Map n to problem parameters deterministically
    if n <= 0:
        return
    N = n
    M = 10 * n

    # Deterministic construction of light positions:
    # strictly increasing, within [1, M-1], and length N
    # Example: spread roughly linearly in [1, M-1]
    if N == 1:
        lights = [M // 2]
    else:
        step = max(1, (M - 1) // (N + 1))
        lights = [step * (i + 1) for i in range(N)]
        # Ensure all lights < M and strictly increasing
        lights = [min(M - 1, lights[i]) for i in range(N)]
        for i in range(1, N):
            if lights[i] <= lights[i - 1]:
                lights[i] = lights[i - 1] + 1
        # Clamp again to keep < M
        for i in range(N - 1, -1, -1):
            if lights[i] >= M:
                lights[i] = M - (N - i)
        if lights[0] <= 0:
            shift = 1 - lights[0]
            lights = [x + shift for x in lights]
        for i in range(1, N):
            if lights[i] <= lights[i - 1]:
                lights[i] = lights[i - 1] + 1
        if lights[-1] >= M:
            diff = lights[-1] - (M - 1)
            lights = [x - diff for x in lights]

    light = [0] + lights + [M]

    sumlist = []
    sumlight = 0
    ans = -10**30

    for i in range(N + 1):
        sumlight += (-1) ** (i + 1) * light[i]
        sumlist.append(sumlight)

    for i in range(1, N + 1):
        if light[i] > light[i - 1] + 1:
            ans = max(ans, 2 * sumlist[i - 1] - sumlight + (-1) ** (i + 1) * (light[i] - 1))
        if light[i] < light[i + 1] - 1:
            ans = max(ans, 2 * sumlist[i] - sumlight + (-1) ** i * (light[i] + 1))

    if N % 2 == 0:
        result = max(ans, sumlight + M)
    else:
        result = max(ans + M, sumlight)

    print(result)


if __name__ == "__main__":
    main(5)