from collections import defaultdict, deque
import random
import string

inf = 100000000000000000  # 1e17
mod = 998244353


def build_tran_dict():
    tran = defaultdict(int)
    tran['_'] = 0
    for i in range(97, 97 + 26):
        tran[chr(i)] = i - 96
    return tran


TRAN_dict = build_tran_dict()


def cal(X):
    base = 1
    number = 0
    for x in X:
        number = number * base + TRAN_dict[x]
        base *= 27
    return number


def check(X, result, stone):
    number = cal(X)
    if number in stone:
        result.append(stone[number])


def generate_test_data(n, max_k=5):
    # 随机生成测试数据：n 个石头，m 条规则，字符串长度 k
    # 为了方便，固定所有字符串长度相同
    k = random.randint(1, max_k)
    m = random.randint(n, n * 2)  # 适度生成一些规则

    # 生成所有石头字符串（用小写字母）
    M = set()
    while len(M) < n:
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(k))
        M.add(s)
    M = list(M)

    # 构建 STONE 表，方便生成一致的规则
    stone_index = {s: i for i, s in enumerate(M)}

    S = []
    F = []

    # 生成 m 条规则，保证每条规则至少包含其目标石头
    for _ in range(m):
        target_idx = random.randrange(n)
        target_str = M[target_idx]

        # 随机选择一些位置改为 '_'，生成模式
        mask = []
        for ch in target_str:
            if random.random() < 0.5:
                mask.append('_')
            else:
                mask.append(ch)
        pattern = ''.join(mask)

        S.append(pattern)
        F.append(target_idx)

    return n, m, k, M, S, F


def solve(n, m, k, M, S, F):
    STONE = defaultdict(int)
    for i in range(n):
        STONE[cal(list(M[i]))] = i

    bian = [[] for _ in range(n)]
    du = [0] * n

    for i in range(m):
        gain = []
        # 枚举所有可能替换 '_' 的方案
        for digit in range(1 << k):
            now = list(S[i])
            tmp = bin(digit)[2:]
            tmp = '0' * (k - len(tmp)) + tmp
            for j in range(k):
                if tmp[j] == '1':
                    now[j] = '_'
            check(now, gain, STONE)
        if F[i] not in gain:
            return False, []
        for x in gain:
            if x != F[i]:
                bian[F[i]].append(x)
                du[x] += 1

    QUE = deque()
    for i in range(n):
        if du[i] == 0:
            QUE.append(i)
    TOP_SORT = []
    while QUE:
        now = QUE.pop()
        TOP_SORT.append(now)
        for to in bian[now]:
            du[to] -= 1
            if du[to] == 0:
                QUE.append(to)
    if len(TOP_SORT) == n:
        return True, [i + 1 for i in TOP_SORT]
    else:
        return False, []


def main(n):
    # 生成规模为 n 的测试数据并运行原逻辑
    n, m, k, M, S, F = generate_test_data(n)
    ok, order = solve(n, m, k, M, S, F)
    if ok:
        print("YES")
        print(*order)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)