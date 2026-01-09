def main(n):
    # 确定性生成输入数组：长度为 n，元素为 i // 2
    arr = [i // 2 for i in range(n)]

    arr1 = [arr[0]]
    m = -1
    ans = None
    for i, v in enumerate(arr):
        if v > m + 1:
            ans = i + 1
            break
        m = max(m, v)

    else:
        ans = -1

    return ans


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做实验
    result = main(10)
    # print(result)
    pass