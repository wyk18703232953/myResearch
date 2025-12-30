import random

def main(n):
    # 生成测试数据：长度为 n 的数字串 a 和 b，保证没有前导零
    if n <= 0:
        return

    # a 和 b 都为长度为 n 的数字串
    a_str = str(random.randint(10**(n-1), 10**n - 1))
    b_str = str(random.randint(10**(n-1), 10**n - 1))

    a = list(map(int, a_str))
    b = list(map(int, b_str))

    ans = []
    la, lb = len(a), len(b)

    if la != lb:
        # 和原逻辑一致：若长度不同，输出 a 的降序排列
        print("".join(map(str, sorted(a, reverse=True))))
        return

    for i in range(lb):
        if b[i] in a:
            ans.append(b[i])
            a.remove(b[i])
        else:
            # 回退并寻找小于当前 b[i] 的最大可用数字
            while i > -1:
                ma = -1
                for j in a:
                    if j < b[i]:
                        ma = max(ma, j)
                if ma != -1:
                    ans.append(ma)
                    a.remove(ma)
                    break
                i -= 1
                a.append(ans.pop())
            a.sort()
            while a:
                ans.append(a.pop())
            break

    print("".join(str(i) for i in ans))


if __name__ == "__main__":
    # 示例：规模 n = 5，可自行修改
    main(5)