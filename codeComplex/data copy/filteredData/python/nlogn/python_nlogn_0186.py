def main(n):
    from collections import defaultdict

    # Deterministically generate input array a of length n
    # Example: arithmetic progression starting from 1
    a = [i % 10 for i in range(1, n + 1)]

    tot = 0
    for i in range(n):
        l = i
        r = n - i - 1
        tot += a[i] * l + -a[i] * r

    for_cnt = defaultdict(int)

    for i in range(n):
        fault = for_cnt[a[i] - 1] + for_cnt[a[i] + 1] + for_cnt[a[i]]
        tot -= a[i] * fault
        for_cnt[a[i]] += 1

    back_cnt = defaultdict(int)

    i = n - 1
    while i >= 0:
        fault = back_cnt[a[i] - 1] + back_cnt[a[i] + 1] + back_cnt[a[i]]
        tot -= -a[i] * fault
        back_cnt[a[i]] += 1
        i -= 1

    # print(tot)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(1000)