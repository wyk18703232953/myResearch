import random

def main(n: int):
    # 根据规模 n 生成测试数据 a
    # 示例策略：在 [1, 10^n] 范围内随机生成一个整数
    if n <= 0:
        a = 1
    else:
        upper = 10 ** n
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
                o = o + 1
        if o == t:
            l = l + 1

    if l > 0:
        print("YES")
    else:
        print("NO")