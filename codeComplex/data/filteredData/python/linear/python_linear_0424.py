import math

def main(n):
    # 映射：a = n，b 为与运算掩码，l 为长度为 a 的整数列表
    a = n
    if a <= 0:
        return
    b = (a * 37) ^ 12345
    b &= 65535
    if b == 0:
        b = 1

    # 生成确定性数据：l[i] 在 [0, 100000] 范围内
    t_size = 100001
    l = [((i * 31 + 7) * (a + 5)) % t_size for i in range(a)]

    t = [[-1, 0] for _ in range(t_size)]

    for i in range(a):
        if t[l[i]][0] != -1:
            # print(0)
            pass
            return
        t[l[i]][0] = 3

    s = math.inf
    for i in range(a):
        key = l[i] & b
        if key < t_size and t[key][0] != -1:
            if key != l[i] and t[key][0] != 1:
                t[key] = [1, min(2, t[key][1] + 1)]

        else:
            if key < t_size:
                t[key] = [2, 1]

    for i in range(a):
        key = l[i] & b
        if key < t_size and t[key][1] != 0 and t[key][0] == 1:
            s = min(s, t[key][1])

    if s == math.inf:
        # print(-1)
        pass

    else:
        # print(s)
        pass
if __name__ == "__main__":
    main(10000)