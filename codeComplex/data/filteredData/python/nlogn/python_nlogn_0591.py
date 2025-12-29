import random

def main(n: int):
    # 1. 生成测试数据
    # 规模参数 n 作为数组长度，m 在原程序中未使用，仅形式存在
    m = random.randint(1, max(1, n))  # 保留 m 的生成以模拟原输入结构（虽然用不到）
    
    # 生成 n 个整数，范围可按需调整
    # 这里设定为 [-10^6, 10^6]，包含负数和正数，覆盖多种情况
    a = [random.randint(-10**6, 10**6) for _ in range(n)]

    # 2. 原始逻辑
    a.sort()
    mx = a[-1]
    t = 0
    ans = 0
    for i in a:
        if i > 0:
            if i > t:
                t += 1
            ans += i - 1
    ans -= mx - t

    # 3. 输出结果
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)