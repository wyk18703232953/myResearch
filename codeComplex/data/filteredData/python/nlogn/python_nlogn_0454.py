import random

def main(n):
    # 生成测试数据：1..n 的随机排列，随机选择 m
    p = list(range(1, n + 1))
    random.shuffle(p)
    m = random.choice(p)

    mindex = p.index(m)
    ldict = {}
    rdict = {}
    diff = 0
    ans = 0
    ldict[0] = 1
    rdict[0] = 1

    # 左侧
    for i in range(mindex - 1, -1, -1):
        if p[i] < m:
            diff -= 1
        else:
            diff += 1
        if diff in ldict:
            ldict[diff] += 1
        else:
            ldict[diff] = 1

    # 右侧
    diff = 0
    for i in range(mindex + 1, n):
        if p[i] < m:
            diff -= 1
        else:
            diff += 1
        if diff in rdict:
            rdict[diff] += 1
        else:
            rdict[diff] = 1

    # 统计答案
    for num in ldict:
        if -num in rdict:
            ans += ldict[num] * rdict[-num]
        if -num + 1 in rdict:
            ans += ldict[num] * rdict[-num + 1]

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n = 10
    main(10)