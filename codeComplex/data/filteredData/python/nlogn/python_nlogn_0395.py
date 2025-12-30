import heapq
import random


def main(n):
    # 生成规模为 n 的测试数据
    # 随机生成 k（0 <= k <= n）
    k = random.randint(0, n) if n > 0 else 0

    # 生成 p 和 c，元素范围可按需调整
    p = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 原始逻辑开始
    p_with_index = sorted([(x, i) for i, x in enumerate(p)], key=lambda x: x[0])

    ans = []
    top_k = []

    cur_gold = 0
    for i, t in enumerate(p_with_index):
        idx = t[1]
        if k == 0:
            ans.append((c[idx], idx))
        else:
            if i < k:
                cur_gold += c[idx]
                ans.append((cur_gold, idx))
                heapq.heappush(top_k, c[idx])
            else:
                smallest = heapq.nsmallest(1, top_k)[0]
                if smallest < c[idx]:
                    cur_gold += c[idx]
                    ans.append((cur_gold, idx))
                    heapq.heappop(top_k)
                    heapq.heappush(top_k, c[idx])
                    cur_gold -= smallest
                else:
                    ans.append((cur_gold + c[idx], idx))

    ans = sorted(ans, key=lambda x: x[1])
    result = " ".join(str(x[0]) for x in ans)
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可自行修改 n
    main(10)