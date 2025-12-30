import sys
from typing import Tuple


def pprint(s):
    sys.stdout.write(str(s) + "\n")


def solve(n: int, d: int, k: int):
    # 输出树结构（边），逻辑保持与原程序一致
    for i in range(1, d + 1):
        pprint(str(i) + " " + str(i + 1))
        if i + 1 == n:
            return

    q = d + 2
    for i in range(2, d + 1):
        for _ in range(k - 2):
            pprint(str(i) + " " + str(q))
            if q == n:
                return
            q += 1

            def rec(depth, current, head):
                if depth == 0:
                    return current

                for _inner in range(k - 1):
                    pprint(str(head) + " " + str(current))
                    if current == n:
                        return current
                    current += 1

                    current = rec(depth - 1, current, current - 1)
                    if current == n:
                        return current

                return current

            if i <= (d + 2) / 2:
                depth = i - 2
            else:
                depth = d - i

            q = rec(depth, q, q - 1)
            if q == n:
                return


def max_nodes(d: int, k: int) -> int:
    # 与原代码一致的可构造最大节点数计算
    q = k - 1
    if k == 2:
        return d + 1

    if d % 2:
        # d 为奇数
        return (q * (1 - q ** (d // 2)) // (1 - q) + 1) * 2
    else:
        # d 为偶数
        return (q * (1 - q ** (d // 2 - 1)) // (1 - q) + 1) * 3 + 1


def gen_params(n: int) -> Tuple[int, int]:
    """
    根据规模 n 生成 (d, k)，保证：
    - 2 <= d < n
    - k >= 2
    - n <= max_nodes(d, k) 时输出 YES 并构造，否则输出 NO。
    策略：从小 d,k 开始枚举，找到第一个满足 n <= maxi 的组合。
    如果找不到则退化到一个简单组合（例如链状树 k=2, d=n-1），并输出 NO。
    """
    # 限制 d 的搜索范围到一个较小值，防止无意义的大 d
    max_d = min(n - 1, 50)
    for d in range(2, max_d + 1):
        # k=2 的情况最大节点为 d+1，因此只对 n<=d+1 有意义
        # 我们希望覆盖更大 n，优先尝试 k>=3
        for k in range(3, 20):
            if n <= max_nodes(d, k) and n > d:
                return d, k

    # 如果上面没找到合适的，回退到简单参数：
    # 链状树：k=2, 任意 d<n 时最多 d+1 个节点
    # 为了保持与原逻辑一致，此时不会满足 n<=max_nodes，属于 NO 情况。
    d = max(2, min(n - 1, 10))
    k = 2
    return d, k


def main(n: int):
    """
    入口函数：
    1. 根据 n 生成测试参数 d, k
    2. 按原逻辑判断是否可构造
    3. 输出 "NO" 或 "YES" + 构造出的边
    """
    if n <= 2:
        # 原逻辑要求 n > d 且 d>=2，因此 n<=2 时一定 NO
        pprint("NO")
        return

    d, k = gen_params(n)
    maxi = max_nodes(d, k)

    if n > maxi or n <= d:
        pprint("NO")
    else:
        pprint("YES")
        solve(n, d, k)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 做本地测试
    # main(10)
    pass