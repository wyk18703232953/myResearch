import random

def main(n: int) -> int:
    # 生成测试数据：n 个 1..10^9 之间的随机整数
    l = [random.randint(1, 10**9) for _ in range(n)]

    l.sort()
    vis = [0] * n
    ans = 0
    for i in range(n):
        if vis[i] == 0:
            ans += 1
            x = l[i]
            for j in range(n):
                if l[j] % x == 0:
                    vis[j] = 1
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    result = main(10)
    print(result)