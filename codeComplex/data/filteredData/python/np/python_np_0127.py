import math

def main(n):
    # n is the length of the arrays
    if n <= 0:
        print(-1)
        return

    # Deterministic data generation
    larr = [(i % 10) + 1 for i in range(1, n + 1)]
    carr = [(i * 3) % 7 + 1 for i in range(1, n + 1)]

    dic = {0: 0}

    for i in range(n):
        l, c = larr[i], carr[i]
        ndic = dic.copy()
        for j in dic:
            now = math.gcd(j, l)
            if now not in ndic:
                ndic[now] = c + dic[j]
            else:
                ndic[now] = min(ndic[now], dic[j] + c)
        dic = ndic

    print(dic.get(1, -1))


if __name__ == "__main__":
    main(10)