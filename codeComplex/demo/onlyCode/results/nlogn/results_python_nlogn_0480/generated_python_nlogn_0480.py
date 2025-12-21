def main(n):
    m = n * 2
    a = [i % 100 + 1 for i in range(m)]
    dic = {}
    for i in range(m):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    for i in range(1, 102):
        r = 0
        for j in dic:
            r += dic[j] // i
        if r < n:
            return i - 1

if __name__ == "__main__":
    print(main(10))