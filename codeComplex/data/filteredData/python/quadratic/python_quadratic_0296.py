def main(n):
    arr = [i % (max(1, n // 3)) for i in range(n)]
    ans = 0
    while len(arr) != 0:
        e = arr.pop(0)
        if e in arr:
            ans += arr.index(e)
            arr.remove(e)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)