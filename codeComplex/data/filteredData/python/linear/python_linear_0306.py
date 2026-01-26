def main(n):
    # 确定性生成输入数组：长度为 n，第 i 个元素为 i*i + n
    arr = [i * i + n for i in range(n)]

    # 保持原算法逻辑
    for i in range(n):
        arr[i] = (arr[i] - i) // n + (1 if (arr[i] - i) % n > 0 else 0)

    # 返回结果而不是直接打印，方便实验调用
    return arr.index(min(arr)) + 1


if __name__ == "__main__":
    # 示例调用
    result = main(10)
    # print(result)
    pass