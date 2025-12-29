import random

def check(a, b):
    # a, b are strings like "1m", "9p"
    if a[1] == b[1] and 1 <= abs(int(b[0]) - int(a[0])) <= 2:
        return True
    return False

def main(n):
    """
    n: 生成数据的规模，此处理解为生成 n 张牌，然后只取前 3 张按原逻辑处理。
    """
    # 定义所有可能的牌（假设 1-9，花色 m,p,s 可选）
    suits = ['m', 'p', 's']
    tiles = [str(v) + s for v in range(1, 10) for s in suits]

    # 生成 n 张牌（允许重复）
    arr = [random.choice(tiles) for _ in range(max(n, 3))]  # 至少生成 3 张

    # 原程序只处理 3 个牌
    arr = arr[:3]

    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    mineq = 3 - max(d.values())

    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])

    if check(arr[0], arr[1]) or check(arr[1], arr[2]):
        mineq = min(mineq, 1)

    if (arr[0][1] == arr[1][1] == arr[2][1] and
        int(arr[2][0]) - int(arr[1][0]) == 1 and
        int(arr[1][0]) - int(arr[0][0]) == 1):
        mineq = 0

    print(mineq)

# 示例调用
if __name__ == "__main__":
    main(10)