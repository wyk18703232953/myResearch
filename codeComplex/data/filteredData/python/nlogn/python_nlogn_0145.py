def main(n):
    k = 2
    arr = [(i * 3) % (5 * n + 7) + 1 for i in range(n)]
    arr.sort(reverse=True)
    dic = {}
    for a in arr:
        if a * k not in dic:
            dic[a] = 1
    # print(len(dic))
    pass
if __name__ == "__main__":
    main(10)