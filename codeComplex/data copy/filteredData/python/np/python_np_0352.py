from itertools import combinations

MOD = 1000000007

def findsum(comb):
    s = 0
    for song in comb:
        s += song[0]
    return s

def finda(a, b, c, memo):
    key = (a, b, c, 'a')
    if key in memo:
        return memo[key]
    if a == 0:
        memo[key] = 0
        return 0
    if a == 1 and b == 0 and c == 0:
        memo[key] = 1
        return 1
    res = (a * findb(a - 1, b, c, memo) + a * findc(a - 1, b, c, memo)) % MOD
    memo[key] = res
    return res

def findb(a, b, c, memo):
    key = (a, b, c, 'b')
    if key in memo:
        return memo[key]
    if b == 0:
        memo[key] = 0
        return 0
    if b == 1 and a == 0 and c == 0:
        memo[key] = 1
        return 1
    res = (b * finda(a, b - 1, c, memo) + b * findc(a, b - 1, c, memo)) % MOD
    memo[key] = res
    return res

def findc(a, b, c, memo):
    key = (a, b, c, 'c')
    if key in memo:
        return memo[key]
    if c == 0:
        memo[key] = 0
        return 0
    if c == 1 and a == 0 and b == 0:
        memo[key] = 1
        return 1
    res = (c * finda(a, b, c - 1, memo) + c * findb(a, b, c - 1, memo)) % MOD
    memo[key] = res
    return res

def generate_data(n):
    # n is the number of songs
    # T is deterministically tied to n to keep behavior repeatable
    T = 3 * n
    songs = []
    for i in range(1, n + 1):
        t = (2 * i) % (4 * n + 1)
        if t == 0:
            t = 1
        g = (i % 3) + 1
        songs.append([t, g])
    return n, T, songs

def core_logic(n, T, songs):
    total_combinations = 0
    memo = {}
    for i in range(1, n + 1):
        allcomb = combinations(songs, i)
        for comb in allcomb:
            s = findsum(comb)
            if s == T:
                a = 0
                b = 0
                c = 0
                for song in comb:
                    if song[1] == 1:
                        a += 1
                    elif song[1] == 2:
                        b += 1
                    else:
                        c += 1
                total_combinations += (
                    finda(a, b, c, memo)
                    + findb(a, b, c, memo)
                    + findc(a, b, c, memo)
                )
                total_combinations %= MOD
    return total_combinations % MOD

def main(n):
    n, T, songs = generate_data(n)
    result = core_logic(n, T, songs)
    print(result)

if __name__ == "__main__":
    main(5)