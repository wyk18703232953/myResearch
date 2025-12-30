from collections import defaultdict, Counter, deque
import heapq
import random
import string

inf = float('inf')
ninf = float('-inf')

M1 = 10**9 + 7
M2 = 998244353


def pre():
    "Start"
    pass


def solve(a: str, b: str) -> int:
    n = len(a)
    if len(a) < len(b):
        a_sorted = sorted(list(a), reverse=True)
        return int("".join(a_sorted))

    b_int = int(b)
    ans = 0
    cnt = [0] * 10
    for i in range(n):
        cnt[ord(a[i]) - ord('0')] += 1

    def getrem(k):
        cnt[k] -= 1
        res = ""
        for i in range(10):
            if cnt[i] > 0:
                res += str(i) * cnt[i]
        cnt[k] += 1
        return res

    prev = ""
    for i in range(n):
        for j in range(9, -1, -1):
            if cnt[j] > 0:
                newval = prev + str(j) + getrem(j)
                if int(newval) <= b_int:
                    ans = max(ans, int(newval))
                    prev += str(j)
                    cnt[j] -= 1
                    break
    return ans


def main(n: int):
    """
    n: 规模参数，表示生成的数字长度（同时作为 a 和 b 的长度上限）。
    逻辑：
    - 生成长度为 n 的数字串 a（首位不为 0）
    - 生成一个整数 b，长度 <= n，且随机不小于某个下界
    - 调用 solve(a, b) 并打印结果
    """
    if n <= 0:
        return

    # 生成长度为 n 的数字串 a，首位不为 0
    first_digit = random.randint(1, 9)
    rest = [str(random.randint(0, 9)) for _ in range(n - 1)]
    a = str(first_digit) + "".join(rest)

    # 生成 b：长度在 1..n 之间
    len_b = random.randint(1, n)
    first_digit_b = random.randint(1, 9)
    rest_b = [str(random.randint(0, 9)) for _ in range(len_b - 1)]
    b = str(first_digit_b) + "".join(rest_b)

    # 输出输入数据和结果，方便验证
    print("a =", a)
    print("b =", b)
    ans = solve(a, b)
    print(ans)


if __name__ == "__main__":
    pre()
    # 示例：调用 main(5)
    main(5)