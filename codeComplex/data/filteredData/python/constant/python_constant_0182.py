import random

def main(n: int):
    # 根据规模 n 生成测试数据 (l, r)
    # 这里简单设定：l 在 [1, n-1] 中随机，r 在 [l, min(l+5, n)] 中随机
    if n < 3:
        # 对于太小的 n，直接构造一个简单区间
        l, r = 1, 3
    else:
        l = random.randint(1, max(1, n - 1))
        r = random.randint(l, min(l + 5, n))

    # 以下是原逻辑
    if r == l + 1 or r == l:
        print(-1)
    elif l % 2 == 0:
        print(l, l + 1, l + 2)
    elif abs(r - l) >= 3:
        print(l + 1, l + 2, l + 3)
    else:
        print(-1)


# 示例：直接运行时可以指定一个规模
if __name__ == "__main__":
    main(10)