import random

mod = 1000000007

def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans

def main(n):
    # 生成测试数据：n 个 1~n 之间的随机整数
    a = [random.randint(1, n) for _ in range(n)]
    a.sort()

    i = 0
    ans = 0
    while i < len(a):
        if a[i]:
            ans += 1
            j = i + 1
            while j < n:
                if a[j] % a[i] == 0:
                    a[j] = 0
                j += 1
        i += 1
    print(ans)