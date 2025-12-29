import random

def main(n, seed=0):
    random.seed(seed)

    # 生成测试数据
    # m 为总预算上限，a_i, b_i 为随机生成的值
    # 确保有一定比例的数据可行
    arr = []
    brr = []
    for _ in range(n):
        a = random.randint(1, 1000)
        b = random.randint(1, a)  # b 不大于 a，避免负差距过多
        arr.append(a)
        brr.append(b)

    # 让 m 大致落在 sum(brr) 和 sum(arr) 之间，保证有一定概率可行又需要压缩
    sun = sum(arr)
    su = sum(brr)
    if su >= sun:
        # 特殊情况：b 的总和 >= a 的总和，设 m 在 [su, sun] 区间内任取
        m = random.randint(su, sun)
    else:
        # 一般情况：m 在 [su, sun] 区间内任取
        m = random.randint(su, sun)

    # 以下是原逻辑的实现
    sun, su, ans = 0, 0, 0
    dif = []
    for a, b in zip(arr, brr):
        sun += a
        su += b
        dif.append(a - b)

    if su > m:
        print(-1)
    elif sun == m:
        print(0)
    else:
        dif.sort()
        j = n - 1
        while sun > m and j >= 0:
            sun -= dif[j]
            ans += 1
            j -= 1
        # 按原逻辑假设一定能成功压缩到 <= m，这里直接输出 ans
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)