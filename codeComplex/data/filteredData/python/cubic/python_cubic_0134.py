import random
import string

class NextStringIndex:
    def __init__(self, string):
        self.INF = 10 ** 9
        self.alph = "abcdefghijklmnopqrstuvwxyz"
        self.kind = len(self.alph)
        self.to_ind = {char: ind for ind, char in enumerate(self.alph)}

        self.string = string
        self.len_s = len(string)
        self.next_ = self.make_next()

    def __getitem__(self, tup):
        ind, char = tup
        return self.next_[ind][self.to_ind[char]]

    def make_next(self):
        dp = [[self.INF] * self.kind for _ in range(self.len_s + 1)]
        # 预处理每个位置之后每个字符的下一次出现位置
        for i in range(self.len_s - 1, -1, -1):
            for j, char in enumerate(self.alph):
                if self.string[i] == char:
                    dp[i][j] = i + 1
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp


def solve(t1, t2, len_s, s_next):
    INF = 10 ** 9
    len_t1 = len(t1)
    len_t2 = len(t2)
    dp = [[INF] * (len_t2 + 1) for _ in range(len_t1 + 1)]
    dp[0][0] = 0

    for i in range(len_t1 + 1):
        for j in range(len_t2 + 1):
            length = dp[i][j]
            if length > len_s:
                continue
            if i < len_t1 and s_next[length, t1[i]] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], s_next[length, t1[i]])
            if j < len_t2 and s_next[length, t2[j]] < INF:
                dp[i][j + 1] = min(dp[i][j + 1], s_next[length, t2[j]])

    return dp[-1][-1] < INF


def generate_test_case(n):
    # n 为规模，用来控制字符串大致长度
    # 这里简单设定：
    #   |s| ~ n
    #   |t| ~ n
    len_s = n
    len_t = n

    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
    return s, t


def main(n):
    # 使用 n 控制测试数据组数和每组的字符串规模
    # 例如：生成 n 组测试，每组字符串长度约为 n
    results = []
    for _ in range(n):
        s, t = generate_test_case(n)
        len_s = len(s)
        len_t = len(t)

        s_next = NextStringIndex(s)

        flag = False
        for i in range(len_t + 1):
            if solve(t[0:i], t[i:], len_s, s_next):
                flag = True
                break
        results.append("YES" if flag else "NO")

    # 输出所有结果
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3 组规模为 3 的随机测试数据并运行
    main(3)