def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 这里选择 a[i] = i + 1，使得输入规模和内容完全由 n 决定
    a = [i + 1 for i in range(n)]
    s = sum(a)
    new = 0
    i = 0
    # 保持原有算法逻辑不变
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1
    # 为了便于实验，返回结果而不是直接打印
    return i + 1


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值进行实验
    result = main(10)
    print(result)