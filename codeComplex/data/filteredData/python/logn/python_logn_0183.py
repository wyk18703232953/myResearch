import random

def main(n: int):
    # 根据 n 生成测试数据，这里生成 s，使得 0 <= s <= 9*n
    # 原题中 s 是从输入读取的一个整数，这里用可复现的方式生成
    random.seed(0)
    s = random.randint(0, 9 * n if n > 0 else 0)

    def check(x: int) -> bool:
        y = list(str(x))
        ans = x
        for i in y:
            ans -= int(i)
        if ans >= s:
            return True
        return False

    ans = 0
    l = 1
    r = n
    while l <= r:
        m = (l + r) // 2
        if check(m):
            ans = n - m + 1
            r = m - 1
        else:
            l = m + 1

    print(ans)


if __name__ == "__main__":
    # 示范调用，规模 n 可自行调整
    main(10**6)