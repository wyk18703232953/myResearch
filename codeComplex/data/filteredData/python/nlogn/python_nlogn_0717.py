import random

def shuntsu(li):
    li.sort()
    return (li[0][1] == li[1][1] and
            li[1][1] == li[2][1] and
            int(li[1][0]) == int(li[0][0]) + 1 and
            int(li[2][0]) == int(li[1][0]) + 1)

def solve(l):
    if l[0] == l[1] and l[1] == l[2]:
        return 0
    if shuntsu(l[:]):
        return 0
    for k in l:
        if len([x for x in l if x == k]) > 1:
            return 1
        if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 1]) != 0:
            return 1
        if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 2]) != 0:
            return 1
    return 2

def gen_test_data(n):
    # n 控制生成的候选牌数量，从中取前3个作为输入
    # 牌格式为 "1m"~"9m","1p"~"9p","1s"~"9s"
    suits = ['m', 'p', 's']
    tiles = [str(v) + s for v in range(1, 10) for s in suits]
    res = []
    for _ in range(max(3, n)):
        res.append(random.choice(tiles))
    return res[:3]

def main(n):
    l = gen_test_data(n)
    ans = solve(l)
    print(ans)

if __name__ == "__main__":
    # 示例：规模参数可自行调整
    main(10)