import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例为：a, b 是 [0, 2^n - 1] 范围内的随机整数
    # 并且保证 a <= b（若原题没有此限制，可去掉这行排序逻辑）
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)
    if a > b:
        a, b = b, a

    K = 60
    if a == b:
        ans = 0
    else:
        curr = K
        while (b & (1 << curr)) == (a & (1 << curr)):
            curr -= 1
        ans = (1 << curr)
        curr -= 1
        lb = False
        ga = False
        for i in range(curr, -1, -1):
            if (b & (1 << i)) == 0 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True
                else:
                    ans += (1 << i)
            elif (b & (1 << i)) == 0 and (a & (1 << i)) == 1:
                ans += (1 << i)
            elif (b & (1 << i)) == 1 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True
                    lb = True
                else:
                    ans += (1 << i)
            else:
                if not lb:
                    ans += (1 << i)
                    lb = True
                else:
                    ans += (1 << i)

    print(ans)


if __name__ == '__main__':
    # 示例调用：可以根据需要修改 n
    main(10)