import random

def f(a, b):
    global ans
    maks = max(a, b)
    mins = min(a, b)
    ans += (maks // mins)
    if mins == 1:
        return ans
    else:
        if maks % mins == 0:
            return ans
        else:
            return f(maks % mins, mins)

def main(n):
    """
    n 为测试数据规模，表示生成 n 组 (a, b) 进行测试并输出结果。
    测试数据生成方式：a, b 为 [1, 10^6] 范围内的随机正整数。
    """
    random.seed(0)
    for _ in range(n):
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        # 确保不出现 0
        if a == 0: a = 1
        if b == 0: b = 1
        global ans
        ans = 0
        print(f(a, b))

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)