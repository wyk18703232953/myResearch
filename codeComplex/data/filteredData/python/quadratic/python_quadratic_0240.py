import random

def main(n: int):
    # 生成测试数据：ls1 为 1..n 的随机排列，ls2 为 1..10 的随机权值
    ls1 = list(range(1, n + 1))
    random.shuffle(ls1)
    ls2 = [random.randint(1, 10) for _ in range(n)]

    ans = float('inf')

    for i in range(1, n - 1):
        l = [ls2[j] for j in range(0, i) if ls1[j] < ls1[i]]
        r = [ls2[j] for j in range(i + 1, n) if ls1[j] > ls1[i]]

        if l and r:
            ans = min(ans, min(l) + min(r) + ls2[i])

    print([-1, ans][ans != float('inf')])

if __name__ == "__main__":
    # 示例：可修改这里的规模进行快速测试
    main(5)