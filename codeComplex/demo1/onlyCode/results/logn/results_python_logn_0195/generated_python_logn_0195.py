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
    # 约定：s 为 1 到 n 之间的某个值（这里取中间值）
    s = max(1, n // 2)

    # 执行原逻辑
    result = max(0, n - binsearch(n, s))
    print(result)

# 示例调用
if __name__ == "__main__":
    # 这里给一个默认的 n，实际使用时可在外部按需调用 main(n)
    main(10)