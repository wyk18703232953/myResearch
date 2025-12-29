import math
import random

# decimal to binary
def binary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def decimal(s):
    return int(s, 2)

# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

# if number is prime in √n time
def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

# list to string ,no spaces
def lts(l):
    return ''.join(map(str, l))

# String to list
def stl(s):
    return list(s)

# Returns list of numbers with a particular sum
def sq(a, target, arr=None):
    if arr is None:
        arr = []
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return None
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans
    return None

# Sieve for prime numbers in a range
def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return cnt

# for positive integers only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里我们生成一个长度为 n 的合法括号串（n 为偶数），
       然后按原逻辑选出长度为 k 的子序列。
    """
    if n < 2:
        # 没有足够长度生成括号串，直接返回
        print("")
        return

    # 确保 n 为偶数，括号总数为 n
    if n % 2 == 1:
        n -= 1
    if n <= 0:
        print("")
        return

    # 生成一个合法括号串 s，长度为 n
    # 简单方式：先生成 n//2 个 "(" 和 n//2 个 ")"，再打乱并调整成合法括号串
    half = n // 2
    s_list = ["("] * half + [")"] * half
    random.shuffle(s_list)

    # 调整为合法括号串：贪心修正
    balance = 0
    for i in range(n):
        if s_list[i] == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            # 不合法：在当前位置之前找一个 "(" 换过来
            for j in range(i + 1, n):
                if s_list[j] == "(":
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    balance = 0  # 重算 balance
                    for k in range(i + 1):
                        balance += 1 if s_list[k] == "(" else -1
                    break

    # 再次确保整体合法：末尾平衡应为 0
    # 若仍不合法，退化为简单合法串
    balance = 0
    ok = True
    for ch in s_list:
        balance += 1 if ch == "(" else -1
        if balance < 0:
            ok = False
            break
    if not ok or balance != 0:
        s_list = ["("] * half + [")"] * half
    s = lts(s_list)

    # 选取 k：按原题一般做法，k 是不超过 n 的偶数
    # 这里设 k = n//2*2（最大不超过 n 的偶数）
    k = n if n % 2 == 0 else n - 1

    ans = []
    lb = k // 2
    rb = k // 2

    for c in s:
        if lb > 0:
            if c == "(":
                lb -= 1
            else:
                rb -= 1
            ans.append(c)
        elif rb > 0:
            if c == ")":
                ans.append(c)
                rb -= 1
        elif lb == 0 and rb == 0:
            break

    print(lts(ans))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)