import random

prime = [True for _ in range(1000001)]

def solve(n, e, h, a, b, c):
    ans = 1e9
    for i in range(1, 1000001):
        su = 0
        ntmp = n
        tmp1 = e
        tmp2 = h
        tmp1 -= i
        tmp2 -= i
        if tmp1 < 0 or tmp2 < 0 or i > ntmp:
            break
        ntmp -= i
        su += c * i
        if ntmp == 0:
            ans = min(ans, su)
            continue
        if a <= b:
            if (tmp1 // 2) >= ntmp:
                su += a * ntmp
                ntmp = 0
            else:
                su += a * (tmp1 // 2)
                ntmp -= (tmp1 // 2)
                if ntmp <= (tmp2 // 3):
                    su += b * ntmp
                    ntmp = 0
                else:
                    su += b * (tmp2 // 3)
                    ntmp -= (tmp2 // 3)
        else:
            if (tmp2 // 3) >= ntmp:
                su += b * ntmp
                ntmp = 0
            else:
                su += b * (tmp2 // 3)
                ntmp -= (tmp2 // 3)
                if ntmp <= (tmp1 // 2):
                    su += a * ntmp
                    ntmp = 0
                else:
                    su += a * (tmp1 // 2)
                    ntmp -= (tmp1 // 2)
        if ntmp == 0:
            ans = min(ans, su)
    if ans == 1e9:
        return -1
    else:
        return ans

def shortest_distinct_substring_length(s):
    n = len(s)
    m = {}
    have = {}
    cc = 0
    for ch in s:
        if ch not in m:
            m[ch] = 1
        else:
            m[ch] += 1
    ct = len(m)
    l = 0
    ans = 1e9
    for i in range(n):
        if s[i] not in have:
            have[s[i]] = 0
            cc += 1
        have[s[i]] += 1
        while l <= i and have[s[l]] > 1:
            have[s[l]] -= 1
            l += 1
        if cc == ct:
            ans = min(ans, i - l + 1)
    return ans

def main(n):
    # 生成测试数据：长度为 n 的随机小写字母串
    random.seed(0)
    s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n))

    # 为 solve 随机生成一组参数（规模与 n 相关）
    dishes = max(1, n // 2)        # n: 要做的菜品数量
    e = n * 2 + 5                  # eggs
    h = n * 2 + 7                  # chocolates
    a = random.randint(1, 10)      # price for one type
    b = random.randint(1, 10)      # price for another type
    c = random.randint(1, 10)      # price for the third type

    cost = solve(dishes, e, h, a, b, c)
    shortest_len = shortest_distinct_substring_length(s)

    print(cost)
    print(shortest_len)

if __name__ == "__main__":
    # 示例：用 n=20 作为规模运行一次
    main(20)