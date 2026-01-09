def main(n):
    m = n
    arr = []
    for i in range(m):
        arr.append([(i + 1), (i + 2)])
    k = 0
    ans = ""
    for i in range(n):
        ans += str(k ^ 1)
        k = k ^ 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)