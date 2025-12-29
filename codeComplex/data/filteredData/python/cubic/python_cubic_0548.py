import random

def main(n: int):
    # 生成测试数据：
    # 1) 生成长度为 n 的数字串 a（不以 0 开头）
    # 2) 生成长度为 m 的数字串 b，m 在 [1, n+1] 之间随机
    # 逻辑与原程序等价：
    # 若 len(a) < len(b): 输出 a 的降序排列
    # 否则按原算法求解

    # 生成 a
    a = [random.randint(1, 9)]  # 首位不为 0
    for _ in range(n - 1):
        a.append(random.randint(0, 9))

    # 生成 b
    m = random.randint(1, n + 1)
    # 保证 b 不以 0 开头
    b = [random.randint(1, 9)]
    for _ in range(m - 1):
        b.append(random.randint(0, 9))

    # 以下为原逻辑，无 input()
    if len(a) < len(b):
        a.sort(reverse=True)
        print(''.join(map(str, a)))
        return
    else:
        ans = -1
        ca = [0] * 10
        for aa in a:
            ca[aa] += 1
        for i in range(len(a)):
            if ca[b[i]]:
                candi = []
                for j in range(i):
                    candi.append(b[j])
                use = -1
                for j in range(b[i] - 1, -1, -1):
                    if ca[j]:
                        use = j
                        ca[j] -= 1
                        candi.append(j)
                        break
                if use < 0:
                    ca[b[i]] -= 1
                    continue
                else:
                    for j in range(9, -1, -1):
                        candi.extend([j] * ca[j])
                    res = int(''.join(map(str, candi)))
                    ans = max(ans, res)
                    ca[use] += 1
                    ca[b[i]] -= 1
            else:
                candi = []
                for j in range(i):
                    candi.append(b[j])
                use = -1
                for j in range(b[i] - 1, -1, -1):
                    if ca[j]:
                        use = j
                        ca[j] -= 1
                        candi.append(j)
                        break
                if use < 0:
                    break
                else:
                    for j in range(9, -1, -1):
                        candi.extend([j] * ca[j])
                    res = int(''.join(map(str, candi)))
                    ans = max(ans, res)
                    ca[use] += 1
                    break

        flg = True
        ca = [0] * 10
        for x in a:
            ca[x] += 1
        for i in range(len(a)):
            if i >= len(b):
                flg = False
                break
            if ca[b[i]]:
                ca[b[i]] -= 1
            else:
                flg = False
                break
        if flg:
            ans = max(ans, int(''.join(map(str, b))))
        print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)