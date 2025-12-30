from collections import deque
import random

def main(n: int):
    # 生成测试数据
    # m: 长度为 n 的整数数组，值在 1..10^9 之间
    m = [random.randint(1, 10**9) for _ in range(n)]
    # s: 长度为 n 的由 '0' 和 '1' 组成的字符串
    s = ''.join(random.choice('01') for _ in range(n))

    a = []
    b = deque()

    i = 1
    for x in m:
        a.append((x, i))
        i += 1
    a.sort(key=lambda p: -p[0])

    ans = []

    for x in s:
        if x == "1":
            v = b.pop()
            ans.append(v[1])
        else:
            v = a.pop()
            ans.append(v[1])
            b.append(v)

    print(*ans)


if __name__ == "__main__":
    # 示例：可按需修改 n
    main(10)