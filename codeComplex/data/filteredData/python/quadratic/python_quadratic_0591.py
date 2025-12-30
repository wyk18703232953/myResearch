import random

def solve_case(n, k, s):
    a = k
    for j in range(n - k + 1):
        a1, a2, a3 = 0, 0, 0
        for jj in range(k):
            ch = s[j + jj]
            if jj % 3 == 0:
                if ch == "R":
                    a2 += 1
                    a3 += 1
                elif ch == "G":
                    a1 += 1
                    a3 += 1
                else:  # 'B'
                    a1 += 1
                    a2 += 1
            elif jj % 3 == 1:
                if ch == "R":
                    a1 += 1
                    a2 += 1
                elif ch == "G":
                    a2 += 1
                    a3 += 1
                else:  # 'B'
                    a3 += 1
                    a1 += 1
            else:  # jj % 3 == 2
                if ch == "R":
                    a1 += 1
                    a3 += 1
                elif ch == "G":
                    a1 += 1
                    a2 += 1
                else:  # 'B'
                    a3 += 1
                    a2 += 1
        a = min(a, a1, a2, a3)
    return a

def main(n):
    # 这里根据规模 n 生成测试数据
    # 设定测试次数 q，并让每个用例长度和 k 与 n 相关
    q = max(1, n // 5)
    print(q)
    for _ in range(q):
        length = max(1, n)           # 字符串长度
        k = max(1, min(length, n // 2 if n >= 2 else 1))  # 子串长度 k
        s = ''.join(random.choice("RGB") for _ in range(length))
        ans = solve_case(length, k, s)
        # 按原始程序的输出风格，仅输出答案
        print(ans)

if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行一次
    main(10)