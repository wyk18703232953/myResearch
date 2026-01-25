def main(n):
    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Generate deterministic dis list of length n
    # Original code uses: dis = [int(x) << 1, ...]
    # We construct base integers deterministically, then shift left by 1
    base_dis = [(i * 3 + 1) for i in range(n)]
    dis = [x << 1 for x in base_dis]

    # Generate deterministic ter string of length n from pattern "GWL"
    pattern = "GWL"
    ter = "".join(pattern[i % 3] for i in range(n))

    st, ans = 0, 0
    time = {'G': 5, 'W': 3, 'L': 1}
    delta = {'G': 1, 'W': 1, 'L': -1}
    hasWater = False
    convert = 0

    for i in range(n):
        st += dis[i] * delta[ter[i]]
        ans += dis[i] * time[ter[i]]

        if ter[i] == 'W':
            hasWater = True
        elif ter[i] == 'G':
            convert += dis[i]

        if st < 0:
            if hasWater:
                ans += (-st) * 3
            else:
                ans += (-st) * 5
            st = 0

        convert = min(convert, st // 2)

    ans -= 4 * convert
    ans -= 2 * (st // 2 - convert)
    result = ans // 2
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)