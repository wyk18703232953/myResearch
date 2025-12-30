import random

def main(n: int) -> int:
    # 生成测试数据：n 个正整数，这里简单用 1..n 的倍数混合
    # 你可以根据需要调整数据生成策略
    data = [random.randint(1, max(1, n)) for _ in range(n)]

    data.sort()
    ans = [0] * n
    col = 0
    for i in range(n):
        if ans[i] == 0:
            col += 1
            ans[i] = 1
            d = data[i]
            for j in range(i + 1, n):
                if data[j] % d == 0:
                    ans[j] = 1
    print(col)
    return col

if __name__ == "__main__":
    # 示例：当作脚本运行时，给一个默认规模
    main(10)