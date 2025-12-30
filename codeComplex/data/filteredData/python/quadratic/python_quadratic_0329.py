# WARNING This code is just for fun. Reading it might give u a brainfreeze

import random

def solve(n, d, k):
    l = []
    i = 1
    if n <= d:
        return "NO", []
    elif k == 1:
        if n > 2:
            return "NO", []
        elif n == 2:
            return "YES", [(1, 2)]
    else:
        n += 1
        flag = False
        while i < min(d + 1, n):
            l.append((i, i + 1))
            i += 1
        i += 1
        cnt1 = 0
        cnt2 = 1
        se = [[2, d + 1, 1]]
        while cnt1 < cnt2:
            start = se[cnt1][0]
            end = se[cnt1][1]
            mode = se[cnt1][2]
            kk = 3
            while (i < n) and (kk <= k):
                if i < n and not flag:
                    j = start
                    while i < n and j < end:
                        if mode == 1:
                            c = min(j - start + 1, end - j)
                        else:
                            c = min(end - j, d - end + j)
                        if c > 1:
                            se.append([i, i + c - 1, 2])
                            cnt2 += 1
                        ki = j
                        while i < n and c > 0:
                            l.append((ki, i))
                            c -= 1
                            ki = i
                            i += 1
                        j += 1
                else:
                    flag = True
                    break
                kk += 1
            cnt1 += 1
        if i < n or flag:
            return "NO", []
        else:
            return "YES", l


def generate_test(n):
    # 根据规模 n 生成一组 (n, d, k)
    # 这里简单生成：d, k 都在 [1, n] 范围内
    if n < 2:
        n = 2
    d = random.randint(1, max(1, n - 1))
    k = random.randint(1, max(1, n // 2))
    return n, d, k


def main(n):
    # 生成测试数据
    n_val, d, k = generate_test(n)

    # 执行原逻辑
    status, edges = solve(n_val, d, k)

    # 输出与原程序风格一致
    print(status)
    if status == "YES":
        for u, v in edges:
            print(u, v)


if __name__ == "__main__":
    # 示例调用：可以自行修改 n 以观察不同规模
    main(10)