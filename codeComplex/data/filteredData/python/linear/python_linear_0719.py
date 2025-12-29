import random

def main(n: int):
    # 生成测试数据：长度为 n 的随机正整数数组
    # 可根据需要调整数据范围
    l = [random.randint(1, 10**9) for _ in range(n)]

    ans = max(l)
    for i in range(n):
        ans = min(ans, l[i] // max(i, n - i - 1) if max(i, n - i - 1) != 0 else ans)
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)