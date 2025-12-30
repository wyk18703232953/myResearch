import random

def main(n: int):
    # 生成一个合法的 c，使得能构造出对应的 l 和 r
    # 做法：随机生成一个排列，然后加上一些随机偏移，保证元素可比较且有一定随机性
    base = list(range(n))
    random.shuffle(base)
    offset = random.randint(0, 5)
    c = [x + offset for x in base]

    # 根据 c 生成 l 和 r
    l = [0] * n
    r = [0] * n
    for i in range(n):
        left_cnt = 0
        for j in range(i):
            if c[j] > c[i]:
                left_cnt += 1
        l[i] = left_cnt

        right_cnt = 0
        for j in range(i + 1, n):
            if c[j] > c[i]:
                right_cnt += 1
        r[i] = right_cnt

    # 原逻辑：给定 n, l, r 判断是否存在数组 c，并尝试还原
    c_recon = [n] * n
    for i in range(n):
        c_recon[i] -= (r[i] + l[i])

    # 验证左边约束
    for i in range(n):
        m = 0
        for j in range(i):
            if c_recon[j] > c_recon[i]:
                m += 1
        if m != l[i]:
            print("NO")
            print("生成的数据不满足左侧约束")
            print("n =", n)
            print("l =", *l)
            print("r =", *r)
            print("c =", *c)
            return

    # 验证右边约束
    for i in range(n):
        m = 0
        for j in range(i + 1, n):
            if c_recon[j] > c_recon[i]:
                m += 1
        if m != r[i]:
            print("NO")
            print("生成的数据不满足右侧约束")
            print("n =", n)
            print("l =", *l)
            print("r =", *r)
            print("c =", *c)
            return

    print("YES")
    print(*c_recon)


# 示例调用
if __name__ == "__main__":
    main(5)