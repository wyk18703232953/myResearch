import random

def main(n):
    # 1. 生成测试数据
    # 控制 a 的位数不超过 n（至少 1 位）
    digits = max(1, n)
    # 生成一个 digits 位的随机正整数 a
    a = random.randint(10**(digits - 1), 10**digits - 1)
    # 生成一个上界 b，保证有一定概率存在可行解
    # 这里让 b 在 [a//2, 10*a] 之间随机
    b = random.randint(max(0, a // 2), max(1, 10 * a))

    # 2. 原逻辑改写（不使用 input）
    a_list = list(str(a))
    a_list.sort()
    ans = []
    while a_list:
        for i in range(len(a_list) - 1, -1, -1):
            c = ans + [a_list[i]] + a_list[:i] + a_list[i+1:]
            if int(''.join(c)) <= b:
                ans.append(a_list[i])
                a_list.pop(i)
                break

    # 3. 输出结果（可根据需要一起输出 a、b 以便调试）
    print('a =', a)
    print('b =', b)
    print('answer =', ''.join(ans))


if __name__ == "__main__":
    # 示例：调用 main，规模参数 n 可自行调整
    main(5)