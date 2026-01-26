def main(n):
    rgb = 'RGB' * 1000
    T = max(1, n // 10)
    results = []
    for q in range(1, T + 1):
        k = max(1, q)
        if k > n:
            k = n
        s = ''.join('RGB'[(i + q) % 3] for i in range(n))
        ans = 3000
        for w in range(3):
            for e in range(n - k + 1):
                temp = 0
                for i in range(k):
                    if s[e + i] != rgb[w + i]:
                        temp += 1
                if temp < ans:
                    ans = temp
        results.append(ans)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(30)