import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]
    # 按原逻辑需要一个长度为 2n 的只含 '0'、'1' 的字符串，
    # 且保证能匹配栈操作：必须有 n 个 '0' 和 n 个 '1'，并且任意前缀中 '1' 的数量不超过 '0'
    # 这就是一个随机合法括号序列（将 '0' 视为 '('，'1' 视为 ')'）
    # 用随机生成的卡特兰序列方式：
    zeros = n
    ones = n
    s_list = []
    balance = 0
    while zeros > 0 or ones > 0:
        if zeros == 0:
            s_list.append('1')
            ones -= 1
            balance -= 1
        elif ones == 0:
            s_list.append('0')
            zeros -= 1
            balance += 1
        else:
            # 随机决定放 0 还是 1，但不能破坏合法性
            if balance == 0:
                # 只能放 0
                s_list.append('0')
                zeros -= 1
                balance += 1
            elif zeros == ones:
                # 必须放 0，否则后面无法匹配完
                s_list.append('0')
                zeros -= 1
                balance += 1
            else:
                if random.randint(0, 1) == 0:
                    s_list.append('0')
                    zeros -= 1
                    balance += 1
                else:
                    s_list.append('1')
                    ones -= 1
                    balance -= 1
    s = ''.join(s_list)

    # 2. 按原程序逻辑执行
    # l: 把数组 a 的值和索引打包，然后按值排序
    l = sorted(zip(a, range(n)))
    p = 0
    ans = [0] * (2 * n)
    st = [0] * n
    ln = 0

    for i in range(2 * n):
        ch = s[i]
        if ch == '0':
            st[ln] = p
            ans[i] = l[p][1] + 1
            ln += 1
            p += 1
        else:
            ans[i] = l[st[ln - 1]][1] + 1
            ln -= 1

    # 输出结果（原程序是 print(*ans)）
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)