import random

def main(n: int):
    # 生成测试数据：
    # 1) a 为长度在 [1, n] 之间的随机数字串（允许前导零）
    # 2) b 的长度至少为 len(a)，最多为 max(len(a), n)，保证有一定约束关系
    la = random.randint(1, max(1, n))
    lb = random.randint(max(1, la), max(la, n))

    a = [str(random.randint(0, 9)) for _ in range(la)]
    b = [str(random.randint(0, 9)) for _ in range(lb)]

    # 以下为原始逻辑改写，无 input()
    if len(a) < len(b) or len(a) == 1:
        print(''.join(sorted(a)[::-1]))
    else:
        ans, tem = 0, []

        for i in range(len(b)):
            for j in range(int(b[i]) - 1, -1, -1):
                if str(j) in a and not (j == i == 0):
                    a.remove(str(j))
                    ans = max(ans, int(''.join(tem) + str(j) + ''.join(sorted(a)[::-1])))
                    a.append(str(j))
                    break

            if b[i] not in a:
                break

            tem.append(b[i])
            a.remove(b[i])

        if tem:
            ans = max(ans, int(''.join(tem)))

        print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)