import random

def main(n):
    # 1. 生成测试数据：随机生成 a，元素范围 [1, n]，长度为 n
    #    需要避免除以 0，所以元素从 1 开始
    a = [random.randint(1, n) for _ in range(n)]

    b = [0] * n
    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    result = ''.join(s)
    print(result)
    return result

# 示例调用：
# main(5)