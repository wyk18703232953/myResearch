import random

def main(n: int):
    # 生成测试数据：构造一个一定有解的实例
    #
    # 思路：先生成一个 1..n 的排列 ans，代表最终的层次/顺序；
    # 然后按照原算法的逆过程，计算出每个位置 i 的 (arr1[i], arr2[i])。
    #
    # 对于一个给定的 ans，设 pos[i] 是下标 i 在“被删除顺序”中的顺位，
    # 每一次删除时，左边/右边还未删除的元素个数就是 arr1[i]/arr2[i]。
    #
    # 我们模拟删除顺序（按层从大到小），反推出 arr1 和 arr2。
    if n <= 0:
        return

    # 生成一个 1..n 的随机排列作为目标答案
    ans = list(range(1, n + 1))
    random.shuffle(ans)

    # 计算删除顺序：每一轮删除所有当前轮次的元素
    # step_order 按删除时间排序记录下标 i 的顺序
    remaining = list(range(n))
    step_order = []
    # 当前轮次从 n 到 1
    for current in range(n, 0, -1):
        to_remove = [i for i in remaining if ans[i] == current]
        # 保存删除顺序
        for i in to_remove:
            step_order.append(i)
        # 实际删除
        remaining = [i for i in remaining if i not in to_remove]

    # 对于每个元素，根据其被删除时，左/右未删元素个数，生成 arr1/arr2
    arr1 = [0] * n
    arr2 = [0] * n
    alive = list(range(n))
    for idx in step_order:
        pos = alive.index(idx)
        arr1[idx] = pos
        arr2[idx] = len(alive) - pos - 1
        alive.pop(pos)

    # 将生成的 arr1 和 arr2 代入原逻辑进行验证
    d = {i: [arr1[i], arr2[i]] for i in range(n)}
    res = [0] * n

    def run():
        for nn in range(n, 0, -1):
            s = []
            for i in d:
                if d[i][0] == d[i][1] == 0:
                    s.append(i)
                    res[i] = nn

            if s:
                for i in s:
                    del d[i]
                for i in d:
                    l = r = 0
                    for j in s:
                        if j < i:
                            l += 1
                        else:
                            r += 1
                    if d[i][0] >= l:
                        d[i][0] -= l
                    else:
                        return False
                    if d[i][1] >= r:
                        d[i][1] -= r
                    else:
                        return False
            else:
                return False
        return True

    ok = run()
    if not ok or 0 in res:
        print("NO")
    else:
        print("YES")
        print(*res, sep=' ')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)