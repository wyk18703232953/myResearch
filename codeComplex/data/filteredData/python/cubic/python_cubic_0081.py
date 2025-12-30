from itertools import product
from typing import List, Tuple
import random


def distance(tree: Tuple[int, int], outbreak: Tuple[int, int]) -> int:
    return abs(tree[0] - outbreak[0]) + abs(tree[1] - outbreak[1])


def shortest_path(tree: Tuple[int, int],
                  outbreaks: List[Tuple[int, int]],
                  min_dst: int) -> int:
    best = float('inf')
    for outbreak in outbreaks:
        if best < min_dst:
            break
        best = min(best, distance(tree, outbreak))
    return best


def main(n: int) -> None:
    # 生成规模为 n 的随机测试数据
    # N: 行数, M: 列数，outbreak_count: 爆发点个数
    N = n
    M = n
    random.seed(0)
    outbreak_count = max(1, n // 2)

    outbreaks: List[Tuple[int, int]] = []
    for _ in range(outbreak_count):
        x = random.randint(1, N)
        y = random.randint(1, M)
        outbreaks.append((x, y))

    last_tree = (1, 1)
    best_dst = 0

    for x, y in product(range(1, N + 1), range(1, M + 1)):
        path_len = shortest_path((x, y), outbreaks, best_dst)
        if path_len > best_dst:
            last_tree = (x, y)
            best_dst = path_len

    print(last_tree[0], last_tree[1])


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10)