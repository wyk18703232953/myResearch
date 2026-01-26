import math
import collections

def main(n):
    # n 表示数组长度，k 设为 n//2（至少为 1）
    if n <= 0:
        # print(0.0)
        pass
        return
    k = max(1, n // 2)

    # 确定性生成测试数据：arr 长度为 n
    # 例如：arr[i] = (i * 3) % 10 + 1
    arr = [((i * 3) % 10) + 1 for i in range(n)]

    ans = 0
    for i in range(n):
        val = arr[i]
        c = 1
        sol = 0
        if c >= k:
            sol = max(sol, val / c)
        for j in range(i + 1, n):
            val += arr[j]
            c += 1
            if c >= k:
                sol = max(sol, val / c)
        ans = max(sol, ans)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)