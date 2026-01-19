N = 10**5 + 5
MOD = 10**9 + 7

freq = [0 for _ in range(N)]

# precompute powers of 2 modulo MOD
p2 = [0 for _ in range(N)]
p2[0] = 1
for i in range(1, N):
    p2[i] = (p2[i - 1] * 2) % MOD


def Calculate_Mobius(limit):
    arr = [1 for _ in range(limit + 1)]
    prime_count = [0 for _ in range(limit + 1)]
    mobius_value = [0 for _ in range(limit + 1)]

    for i in range(2, limit + 1):
        if prime_count[i] == 0:
            for j in range(i, limit + 1, i):
                prime_count[j] += 1
                arr[j] = arr[j] * i

    for i in range(1, limit + 1):
        if arr[i] == i:
            if (prime_count[i] & 1) == 0:
                mobius_value[i] = 1
            else:
                mobius_value[i] = -1
        else:
            mobius_value[i] = 0

    return mobius_value


mobius = Calculate_Mobius(N)


def main(n):
    # reset frequency array for repeatable experiments
    for i in range(N):
        freq[i] = 0

    # deterministically generate input array b of length n
    # values kept in [1, N-1] using a simple modular pattern
    if n <= 0:
        print(0)
        return

    max_val = N - 1
    b = [((i * 2 + 3) % max_val) + 1 for i in range(n)]

    for v in b:
        freq[v] += 1

    ans = 0
    for i in range(1, N):
        cnt = 0
        for j in range(i, N, i):
            cnt += freq[j]

        total_subsequences = p2[cnt] - 1
        ans = (ans + (mobius[i] * total_subsequences) % MOD) % MOD

    ans += MOD
    print(ans % MOD)


if __name__ == "__main__":
    main(1000)