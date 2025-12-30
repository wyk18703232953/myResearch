import random

def main(n):
    # 生成测试数据：
    # 随机生成 n 个整数，并保证升序，模拟原程序中有序数组的常见场景
    # 也可以改成其他生成方式，只要是长度为 n 的整数数组即可
    arr = sorted(random.randint(0, 1000) for _ in range(n))
    
    # 选择 k（1 <= k <= n），这里示例取大约 n/3，至少为 1
    k = max(1, n // 3)

    # 原逻辑开始
    diff = [0] * (n - 1)
    p = arr[-1] - arr[0]
    for i in range(n - 1):
        diff[i] = arr[i + 1] - arr[i]
    diff.sort(reverse=True)
    result = p - sum(diff[:k - 1]) if k > 1 else p

    # 输出结果（也可返回结果，如果需要的话）
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)