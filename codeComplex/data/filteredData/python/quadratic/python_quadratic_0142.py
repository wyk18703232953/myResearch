from itertools import permutations
import random

def main(n: int) -> int:
    # 1. 生成测试数据 a：4 个 n 行 n 列的 0/1 矩阵
    # 原代码是从输入读取 4 个图案，这里随机生成
    a = []
    for _ in range(4):
        grid = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        a.append(grid)

    # 2. 按原逻辑计算答案
    ans = 10 ** 10
    for perm in permutations(a, 4):
        cnt = 0          # 第几块（0,1,2,3）
        total = 0        # 当前排列的代价
        for block in perm:
            if cnt < 2:
                cnt2 = 0
            else:
                cnt2 = 1
            for row in block:
                for q in row:
                    if q != cnt2 % 2:
                        total += 1
                    cnt2 += 1
            cnt += 1
        ans = min(ans, total)

    # 输出结果（也返回，便于调用）
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)