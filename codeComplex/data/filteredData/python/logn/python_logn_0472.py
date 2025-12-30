import random

# 交互器：根据隐藏的 A、B 返回比较结果
# 返回值：
#   1  如果 (A ^ x) > (B ^ y)
#  -1  如果 (A ^ x) < (B ^ y)
#   0  如果 (A ^ x) == (B ^ y)
def judge(x, y, A, B):
    ax = A ^ x
    by = B ^ y
    if ax > by:
        return 1
    elif ax < by:
        return -1
    else:
        return 0

def main(n):
    # 1. 生成隐藏数据 A、B（n 位非负整数）
    max_val = (1 << n) - 1
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)

    # 2. 模拟原交互过程，通过 judge 查询
    # 初次查询：x=0,y=0
    t = judge(0, 0, A, B)

    # s 用来存放每一位的符号关系，大小开到 n+1（下标 0..n）
    s = [0] * (n + 1)
    if t == 1:
        s[n] = 1
    else:
        s[n] = -1

    a = 0
    b = 0

    # 从最高位 n-1 到 1（保持与原逻辑相同，从高位到低位）
    for i in range(n, 0, -1):
        if i == 0:
            break
        bit = 1 << (i - 1)

        # ans1: (a+bit, b)
        ans1 = judge(a + bit, b, A, B)
        # ans2: (a, b+bit)
        ans2 = judge(a, b + bit, A, B)

        if ans1 == -1 and ans2 == 1:
            a += bit
            b += bit
            s[i - 1] = s[i]
        elif ans1 == 1 and ans2 == -1:
            # a, b 不变
            s[i - 1] = s[i]
        else:
            s[i - 1] = ans1
            if s[i] == 1:
                a += bit
            else:
                b += bit

    # 3. 输出结果对比（恢复出的 a,b 和真实 A,B）
    print("n =", n)
    print("Hidden A =", A)
    print("Hidden B =", B)
    print("Recovered a =", a)
    print("Recovered b =", b)
    print("Correct:", (a == A and b == B))


if __name__ == "__main__":
    # 示例：按原代码规模 30 位测试
    main(30)