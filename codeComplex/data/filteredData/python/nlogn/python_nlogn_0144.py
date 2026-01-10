def main(n):
    k = max(1, n // 3)
    arr = [(i * 2 + 1) for i in range(n)]
    arr.sort()
    dic = {}
    for a in arr:
        if a / k not in dic:
            dic[a] = 1
    print(len(dic))


if __name__ == "__main__":
    main(10)