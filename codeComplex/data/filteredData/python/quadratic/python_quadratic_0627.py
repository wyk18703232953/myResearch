import random

def main(n):
    # 生成测试数据：n 个 1~10^9 的随机整数
    arr = [random.randint(1, 10**9) for _ in range(n)]
    color = [0] * n
    arr.sort()

    ans = 0
    for i in range(n):
        if color[i]:
            continue
        ans += 1
        for j in range(i, n):
            if arr[j] % arr[i] == 0:
                color[j] = ans

    print(ans)
    return ans

# 示例：需要时可以手动调用
# main(10)