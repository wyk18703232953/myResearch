def main(n):
    # Ensure n is non-negative and set a minimum length to meaningfully run the loop
    if n < 0:
        n = 0

    # Generate deterministic distances: dis[i] = (i+1) << 1 (same as 2*(i+1)), then doubled again by original lambda
    # Original: dis = list(map(lambda x: int(x) << 1, input().split()))
    # So we generate base numbers [1,2,...,n] and shift left by 1
    dis = [(i + 1) << 1 for i in range(n)]

    # Generate deterministic terrain string ter of length n using pattern over 'G', 'W', 'L'
    terrain_types = ['G', 'W', 'L']
    ter = ''.join(terrain_types[i % 3] for i in range(n))

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

    # Keep a side effect like the original print for observability
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call for testing / benchmarking; adjust n as needed
    main(10)