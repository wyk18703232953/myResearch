import random

def main(n):
    # 生成测试数据：根据规模 n 随机生成两个 [0, 2^n - 1] 范围内的整数
    # 为保证范围合理，限制 n 最大为 60
    n = max(1, min(n, 60))
    l = random.randint(0, (1 << n) - 1)
    r = random.randint(0, (1 << n) - 1)

    # 保持语义：原程序是从输入中读两个数 l, r
    # 下面是原逻辑的封装
    if l == r:
        print("0")
    else:
        i = 0
        j = 0
        ll, rr = l, r  # 如需调试可用
        while l > 0 or r > 0:
            i += 1
            if (l & 1) ^ (r & 1) == 1:
                j = i
            l = l >> 1
            r = r >> 1
        ans = 1
        for _ in range(j):
            ans *= 2
        ans -= 1
        print(ans)

if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)