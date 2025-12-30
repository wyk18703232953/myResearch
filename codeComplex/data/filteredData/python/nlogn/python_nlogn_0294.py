from collections import deque
import random

def main(n):
    # 1. 生成测试数据
    # arr: 长度为 n 的随机整数数组
    arr = [random.randint(1, 10**9) for _ in range(n)]
    # passenger: 长度为 2n 的由 '0' 和 '1' 组成的字符串
    passenger = ''.join(random.choice('01') for _ in range(2 * n))

    # 2. 原逻辑开始
    new_arr = [(value, idx + 1) for idx, value in enumerate(arr)]
    new_arr.sort()  # 按值升序排序

    que = deque()
    ans = [0] * (2 * n)

    left = 0
    right = n - 1
    le = 0  # 当前队列中的元素数量（对应原代码中的 le）

    for i in range(2 * n):
        if passenger[i] == '0':
            ans[i] = new_arr[left][1]
            que.append(new_arr[left][1])
            left += 1
            le += 1
        else:
            if le >= 1:
                ans[i] = que[-1]
                que.pop()
                le -= 1
            else:
                ans[i] = new_arr[right][1]
                que.append(new_arr[right][1])
                right -= 1
                le += 1

    # 输出结果
    print(*ans)


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(5)