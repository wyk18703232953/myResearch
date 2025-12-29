import random

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的正整数数组
    # 可按需要调整数据规模和范围
    nums = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    ans = 10 ** 12
    for idx, num in enumerate(nums):
        dist = max(idx, n - idx - 1)
        # 原代码在 idx 为 0 或 n-1 时 dist 可能为 0，会产生除零错误
        # 若要保持与原程序行为一致，这里直接跳过 dist == 0 的位置
        if dist == 0:
            continue
        curr = num // dist
        ans = min(ans, curr)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)