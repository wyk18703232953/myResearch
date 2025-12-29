import math
import random

def main(n):
    # 生成 n 组测试数据 (a, b)，a,b 为正整数
    # 可根据需求调整数据规模，这里设为 [1, 10^9]
    test_data = []
    for _ in range(n):
        # 确保 a,b > 0
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        test_data.append((a, b))

    # 按原逻辑处理并输出结果
    for a, b in test_data:
        x, y = a, b
        ans = 0
        while x > 0 and y > 0:
            if x >= y:
                ans += x // y
                x = x % y
            else:
                ans += y // x
                y = y % x
        print(ans)


# 示例调用：
# main(5)