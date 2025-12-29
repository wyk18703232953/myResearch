def binsearch(n, s):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        digits = sum(int(i) for i in str(mid))
        if mid - digits >= s:
            right = mid - 1
        else:
            left = mid + 1
    return right

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里设定 s 为 n 的一半（可按需要调整生成规则）
    s = n // 2

    # 原始代码最后输出的是 max(0, n - binsearch(n, s))
    result = max(0, n - binsearch(n, s))
    print(result)

if __name__ == "__main__":
    # 示例：使用某个固定规模来运行
    main(10**6)