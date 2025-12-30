import random

def main(n: int) -> int:
    # 生成测试数据：n 个 1~10^6 之间的随机整数
    l1 = [random.randint(1, 10**6) for _ in range(n)]

    ans = 0
    l1.sort()
    visited = [0] * n

    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans += 1
        for j in range(i + 1, n):
            if visited[j] == 0 and l1[j] % l1[i] == 0:
                visited[j] = 1
    return ans

if __name__ == "__main__":
    # 示例：n = 10
    result = main(10)
    print(result)