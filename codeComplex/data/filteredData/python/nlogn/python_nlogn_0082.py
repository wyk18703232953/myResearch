from random import randint

def main(n, k=None):
    """
    n: 规模（参赛人数）
    k: 名次（1 <= k <= n），若为 None 则随机生成
    """
    # 生成测试数据：n 行，每行两个整数 [x, y]
    # 模拟 Codeforces 形式：x 为题目数量，y 为罚时
    # x 取 0~50，y 取 0~500
    a = [[randint(0, 50), randint(0, 500)] for _ in range(n)]

    if k is None:
        k = randint(1, n)

    # 排序逻辑与原题一致：按 x 降序，y 升序
    a.sort(key=lambda x: (-x[0], x[1]))

    p, t = -1, -1
    ans = 0

    if k <= n:
        p, t = a[k - 1]

    for x, y in a:
        if x == p and y == t:
            ans += 1

    # 输出与原程序一致：只输出答案
    print(ans)


if __name__ == "__main__":
    # 示例：固定规模 n=10，可根据需要修改或在外部调用 main(n, k)
    main(10)