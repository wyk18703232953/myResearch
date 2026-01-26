import math
import copy

def dtb(n): 
    return bin(n).replace("0b","")

def btd(n): 
    return int(n,2)

def main(n):
    # 映射规则：
    # n 为数组长度
    # 令 kk = max(1, n // 3)，保证 1 <= kk <= n
    if n <= 0:
        return

    kk = max(1, n // 3)
    # 生成确定性数组 a，使用简单的算术构造
    # 避免全部相同，保证排序和查找有意义
    a = [(i * 7 + 3) % (n + 5) for i in range(n)]
    c = copy.copy(a)
    a.sort(reverse=True)
    b = []
    f = []
    ans = 0
    for i in range(kk):
        ans += a[i]
        b.append(a[i])
    count = 1
    x = 0
    y = 0
    for i in range(n):
        if len(f) == (kk - 1):
            y = i
            break
        if c[i] in b:
            f.append(i - x + 1)
            x = i + 1
            b.remove(c[i])

    f.append(n - y)

    # print(ans)
    pass
    for i in f:
        # print(i, end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)