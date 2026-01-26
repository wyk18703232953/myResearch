def main(n):
    # n 表示数组长度
    arr = set((i * 2) % (n + 3) for i in range(n))
    # print(len(arr) - (0 in arr))
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)