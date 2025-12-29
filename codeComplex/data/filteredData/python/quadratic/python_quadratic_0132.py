import itertools
import random

def main(n: int) -> int:
    # 生成测试数据：4 个 n×n 的 0/1 字符串网格，中间以空行分隔的输入结构在这里不再需要
    a = []
    for _ in range(4):
        grid = []
        for _ in range(n):
            # 每行一个长度为 n 的 '0'/'1' 字符串
            row = ''.join(random.choice('01') for _ in range(n))
            grid.append(row)
        a.append(grid)

    best = 4 * n * n
    for p in itertools.permutations(a):
        for s in range(2):
            count = 0
            for i in range(4):
                for r in range(n):
                    for c in range(n):
                        expected = str((s + (i // 2 + r) + (i % 2 + c)) % 2)
                        if p[i][r][c] != expected:
                            count += 1
            if count < best:
                best = count

    # 为了兼容原程序的行为，这里既返回结果，又打印结果
    print(best)
    return best

if __name__ == "__main__":
    # 示例：调用 main(3)，实际使用时可按需要修改 n
    main(3)