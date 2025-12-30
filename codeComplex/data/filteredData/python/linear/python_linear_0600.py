import math
import random


def main(n, k=None, edges=None, seed=0):
    random.seed(seed)

    # 若未给出k和edges，则自动生成一个随机树及k
    if k is None:
        # 生成一个较合理的k：1 到 floor(log2(n)) 之间
        max_k = max(1, int(math.log2(n))) if n > 1 else 1
        k = random.randint(1, max_k)

    if edges is None:
        # 生成一棵随机树：n个点，n-1条边
        # 用随机父节点方法生成树
        edges = []
        for v in range(2, n + 1):
            parent = random.randint(1, v - 1)
            edges.append((parent, v))

    # 以下为原算法逻辑（移除 input），封装在 main 中
    degreelist = []
    for _ in range(min(k + 1, math.floor(math.log2(n)) + 10)):
        degreelist.append({})
    degrees = degreelist[0]
    for i in range(1, n + 1):
        degrees[i] = 0
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    small = []
    center = None
    done = False

    for i in range(k):
        if not done:
            small = []
            for guy in degrees:
                if degrees[guy] == 2:
                    print("No")
                    done = True
                    break
                if degrees[guy] == 3:
                    small.append(guy)
                    if center is None:
                        center = guy
                    elif center != guy:
                        print("No")
                        done = True
                        break
                elif degrees[guy] > 1:
                    small.append(guy)
            if done:
                break

            degrees = degreelist[i + 1]

            if center is not None and center not in small:
                if not done:
                    print("No")
                done = True
                break
            elif len(small) == 0:
                if not done:
                    print("No")
                done = True
                break

            for guy in small:
                degrees[guy] = 0
            for u, v in edges:
                if u in degrees and v in degrees:
                    degrees[u] += 1
                    degrees[v] += 1
            for guy in degrees:
                if degrees[guy] > 1 and degreelist[i][guy] != degrees[guy]:
                    if not done:
                        print("No")
                    done = True
                    break
        else:
            break

    if not done:
        if len(degreelist[-1]) == 1:
            print("Yes")
        else:
            print("No")


# 示例调用：main(10)
# 若需要指定 k 和 edges，可直接传入：
# main(n=5, k=2, edges=[(1,2),(2,3),(3,4),(4,5)])