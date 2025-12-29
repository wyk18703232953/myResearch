import random

def solve(n, l, r, x, lis):
    lis = sorted(lis)
    dp = [0]
    dp_low = [0]
    dp_high = [0]
    for i in range(len(lis)):
        # 注意：在遍历 dp 的同时在末尾追加元素，这里使用当前长度避免无限扩展
        current_len = len(dp)
        for j in range(current_len):
            if dp_low[j] == 0:
                dp_low.append(lis[i])
            else:
                dp_low.append(dp_low[j])
            dp_high.append(lis[i])
            dp.append(dp[j] + lis[i])
    count = 0
    for i in range(len(dp)):
        if l <= dp[i] <= r and dp_high[i] - dp_low[i] >= x:
            count += 1
    print(count)


def main(n):
    # 根据规模 n 生成测试数据
    # 约定：n 为元素个数
    # 元素取值在 [1, 10^4] 内
    # l, r, x 也根据 n 和元素值范围自动生成
    
    # 生成随机数组
    max_val = 10_000
    lis = [random.randint(1, max_val) for _ in range(n)]
    total_sum = sum(lis)
    
    # 生成 l, r, x
    # 保证 0 <= l <= r <= total_sum
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum if total_sum > 0 else l)
    x = random.randint(0, max_val)  # 最小最大差
    
    solve(n, l, r, x, lis)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)