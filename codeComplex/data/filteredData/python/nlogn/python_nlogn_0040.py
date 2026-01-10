def main(n):
    # 生成确定性输入数组：长度为 n，元素为 (i % 5) + 1，保证有一定的多样性
    arr = [(i % 5) + 1 for i in range(n)]
    arr = sorted(arr)
    if arr[-1] == 1:
        arr[-1] = 2
    else:
        arr = [1] + arr[:n-1]
    print(*arr)


if __name__ == "__main__":
    main(10)