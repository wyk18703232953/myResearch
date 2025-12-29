import random

def main(n: int):
    # 随机构造测试数据
    # 约定：
    #   m 的规模与 n 同级
    #   k 的规模与 n 同级
    #   a 中元素为 1 ~ 100 的随机整数
    m = random.randint(0, max(1, n * 2))
    k = random.randint(0, max(1, n * 2))
    a = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑
    a.sort()
    r = [x for x in range(n + 1) if sum(a[n - x:]) + k >= m + x]
    ans = min(r) if r else -1
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)