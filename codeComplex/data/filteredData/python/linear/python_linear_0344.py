import random

def main(n):
    # 生成测试数据：
    # 随机生成 d 和一个长度为 n 的严格递增数组 a
    # 保证 a[i] < a[i+1]，以符合原问题中常见的前提
    if n < 2:
        # 原代码假设至少有两个点，否则 pos 初始为 2
        print(2)
        return

    d = random.randint(0, 10)
    a = [0]
    for _ in range(1, n):
        a.append(a[-1] + random.randint(1, 10))

    pos = 2
    for i in range(n - 1):
        l = a[i] + d
        r = a[i + 1] - d
        if l == r:
            pos += 1
        elif l < r:
            pos += 2
    print(pos)

if __name__ == "__main__":
    # 示例：使用 n = 5 运行
    main(5)