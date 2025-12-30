import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里生成 1 到 10^6 之间的随机整数
    a = [random.randint(1, 10**6) for _ in range(n)]

    max1 = float('inf')
    for q in range(len(a)):
        # 对应原程序第一个分支
        if q >= n - q - 1:
            if q != 0:  # 避免除以 0（原程序在 q=0 时会出错）
                max1 = min(max1, min(a[q], a[0]) // q)
        # 对应原程序第二个分支
        if q <= n - q - 1:
            denom = n - q - 1
            if denom != 0:  # 同样避免除以 0
                max1 = min(max1, min(a[q], a[-1]) // denom)

    print(max1)

# 示例调用
if __name__ == "__main__":
    main(10)