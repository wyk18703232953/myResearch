def main(n):
    # 生成确定性的输入数组：长度为 n，元素为 i // 2
    arr = [i // 2 for i in range(n)]
    arr1 = [arr[0]] if arr else []
    m = -1
    for i, v in enumerate(arr):
        if v > m + 1:
            print(i + 1)
            break
        m = max(m, v)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次运行
    main(10)