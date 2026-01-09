def main(n):
    # n 表示数组长度
    arr = set((i * 2) % (n + 1) for i in range(n))
    # print(len(arr) - (0 in arr))
    pass
if __name__ == "__main__":
    main(10)