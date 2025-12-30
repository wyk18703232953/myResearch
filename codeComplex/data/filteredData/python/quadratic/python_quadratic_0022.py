import math
from collections import defaultdict

def Extended_Euclid(n, m):
    stack = []
    while m:
        stack.append((n, m))
        n, m = m, n % m
    if n >= 0:
        x, y = 1, 0
    else:
        x, y = -1, 0
    for i in range(len(stack) - 1, -1, -1):
        n, m = stack[i]
        x, y = y, x - (n // m) * y
    return x, y

class MOD:
    def __init__(self, p, e=1):
        self.p = p
        self.e = e
        self.mod = self.p ** self.e

    def Pow(self, a, n):
        a %= self.mod
        if n >= 0:
            return pow(a, n, self.mod)
        else:
            assert math.gcd(a, self.mod) == 1
            x = Extended_Euclid(a, self.mod)[0]
            return pow(x, -n, self.mod)

    def Build_Fact(self, N):
        assert N >= 0
        self.factorial = [1]
        self.cnt = [0] * (N + 1)
        for i in range(1, N + 1):
            ii = i
            self.cnt[i] = self.cnt[i - 1]
            while ii % self.p == 0:
                ii //= self.p
                self.cnt[i] += 1
            self.factorial.append((self.factorial[-1] * ii) % self.mod)
        self.factorial_inv = [None] * (N + 1)
        self.factorial_inv[-1] = self.Pow(self.factorial[-1], -1)
        for i in range(N - 1, -1, -1):
            ii = i + 1
            while ii % self.p == 0:
                ii //= self.p
            self.factorial_inv[i] = (self.factorial_inv[i + 1] * ii) % self.mod

    def Fact(self, N):
        return self.factorial[N] * pow(self.p, self.cnt[N], self.mod) % self.mod

    def Fact_Inv(self, N):
        if self.cnt[N]:
            return None
        return self.factorial_inv[N]

    def Comb(self, N, K, divisible_count=False):
        if K < 0 or K > N:
            return 0
        retu = self.factorial[N] * self.factorial_inv[K] * self.factorial_inv[N - K] % self.mod
        cnt = self.cnt[N] - self.cnt[N - K] - self.cnt[K]
        if divisible_count:
            return retu, cnt
        else:
            retu *= pow(self.p, cnt, self.mod)
            retu %= self.mod
            return retu

def Bell_Numbers(N, mod, prime=False):
    bell_numbers = [0] * (N + 1)
    bell_numbers[0] = 1
    MD = MOD(mod)
    if prime:
        MD.Build_Fact(min(mod - 2, N - 1))
        for i in range(1, min(mod, N + 1)):
            bell_numbers[i] = sum(bell_numbers[j] * MD.Comb(i - 1, j) for j in range(i)) % mod
        for i in range(mod, N + 1):
            bell_numbers[i] = (bell_numbers[i - mod + 1] + bell_numbers[i - mod]) % mod
    else:
        MD.Build_Fact(N - 1)
        for i in range(1, N + 1):
            bell_numbers[i] = sum(bell_numbers[j] * MD.Comb(i - 1, j) for j in range(i)) % mod
    return bell_numbers

def main(n):
    # 生成测试数据：构造一个 M x N 的字符矩阵，类似原输入
    # 这里将 M 设为 n，列数 N 设为 max(1, n // 2)，使用小写字母循环填充
    M = n
    N = max(1, n // 2)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # 构造 N 行、每行长度为 M 的字符串
    S = []
    for row in range(N):
        row_chars = []
        for col in range(M):
            # 简单模式：依赖行和列索引的字符，保证有一定多样性和重复
            idx = (row * 7 + col * 13) % len(alphabet)
            row_chars.append(alphabet[idx])
        S.append("".join(row_chars))

    # 以下为原逻辑
    dct = defaultdict(int)
    for i in range(M):
        tpl = []
        for j in range(N):
            tpl.append(S[j][i])
        dct[tuple(tpl)] += 1

    ans = 1
    mod = 10 ** 9 + 7
    bell = Bell_Numbers(M, mod)
    for c in dct.values():
        ans *= bell[c]
        ans %= mod
    return ans

if __name__ == "__main__":
    # 示例：可以修改这里的参数进行快速测试
    print(main(5))