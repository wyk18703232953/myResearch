import random

def main(n: int) -> int:
    # 生成测试数据：n 个 1..10^9 之间的随机正整数
    A = [random.randint(1, 10**9) for _ in range(n)]

    A.sort()
    ans = 1
    for i in range(1, n):
        ok = False
        for j in range(i):
            if A[i] % A[j] == 0:
                ok = True
                break
        if not ok:
            ans += 1
    return ans


if __name__ == "__main__":
    # 示例：自行修改 n 的值进行测试
    n = 10
    print(main(n))