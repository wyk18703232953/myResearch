import random

def solve(N, M, B, G):
    B.sort(reverse=True)
    G.sort(reverse=True)

    if B[0] > G[-1]:
        return -1

    boy_capacities = [M - 1] * N
    current_capable_boy_index = 0
    result = sum(B) * M

    for g in G:
        yet = True
        while yet:
            if B[current_capable_boy_index] < g and boy_capacities[current_capable_boy_index] > 0:
                result += g - B[current_capable_boy_index]
                boy_capacities[current_capable_boy_index] -= 1
                yet = False
            elif B[current_capable_boy_index] == g:
                result += g - B[current_capable_boy_index]
                yet = False
            else:
                current_capable_boy_index += 1
                if current_capable_boy_index > N - 1:
                    return -1

    return result


def main(n):
    # 规模解释：
    # N: 男孩数量, M: 每个男孩最多拿的糖果数, G 的长度为 N * M
    # 这里将 n 用作 N，M 简单设为 max(1, n // 2) 以保证有一定规模
    N = max(1, n)
    M = max(1, n // 2)

    # 生成测试数据：
    # B: 男孩基础能力，范围 [1, 10^3]
    # G: 糖果美味度，范围 [1, 10^3]
    B = [random.randint(1, 1000) for _ in range(N)]
    G = [random.randint(1, 1000) for _ in range(N * M)]

    ans = solve(N, M, B, G)
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)