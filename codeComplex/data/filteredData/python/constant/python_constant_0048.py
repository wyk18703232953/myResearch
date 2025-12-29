import random

def main(n: int):
    # 根据规模 n 生成测试数据 a
    # 这里示例：a 在 [1, 10^n] 范围内随机生成（可按需调整生成策略）
    upper = 10 ** max(1, n)
    a = random.randint(1, upper)

    b = str(a)
    c = []
    for i in range(2, a + 1):
        if a % i == 0:
            c.append(i)

    l = 0
    for j in c:
        r = str(j)
        t = len(r)
        o = 0
        for p in r:
            if p == "4" or p == "7":
                o += 1
        if o == t:
            l += 1

    if l > 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行修改
    main(3)