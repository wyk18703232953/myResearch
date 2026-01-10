def main(n):
    from collections import Counter

    # Deterministically generate input array of size n
    # Example pattern: arr[i] = (i % 10) - 5, giving values in range [-5, 4]
    arr = [((i % 10) - 5) for i in range(n)]

    mp = Counter()
    tot, cnt, ans = 0, 0, 0

    for i in arr:
        ncnt = cnt - mp[i] - mp[i + 1] - mp[i - 1]
        ntot = tot - (i * mp[i]) - ((i - 1) * mp[i - 1]) - ((i + 1) * mp[i + 1])
        nsum = (ncnt * i) - ntot
        ans += nsum
        mp[i] += 1
        cnt += 1
        tot += i

    print(ans)


if __name__ == "__main__":
    # Example call for scalability / benchmarking
    main(10**5)