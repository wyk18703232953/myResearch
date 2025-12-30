import random

def main(n: int):
    # 根据规模 n 生成 [l, r] 测试数据
    # 使用 n 作为最大位数，控制数值规模：0 <= l <= r < 2^n
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 原逻辑开始：求在 [l, r] 范围内 bitwise OR 的结果
    bitafter = -1
    for i in range(60, -1, -1):
        if (l & (1 << i)) != (r & (1 << i)):
            bitafter = i
            break

    res = 0
    while bitafter >= 0:
        res += 1 << bitafter
        bitafter -= 1

    print(res)

if __name__ == "__main__":
    # 示例：以 n=10 规模运行一次
    main(10)