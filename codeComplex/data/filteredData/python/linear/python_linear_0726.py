def main(n):
    # 将原来的两个输入 n, k 映射为：n 保持为原 n，k 为 n // 2
    # 这样规模只由单个参数 n 控制
    k = n // 2
    d = (n - k) // 2 + 1
    ans = ['1' if (i + 1) % d == 0 else '0' for i in range(n)]
    result = ''.join(ans)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用：可自行修改 n 观测时间复杂度
    main(10)