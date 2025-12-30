from collections import deque
import random

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 约定：q 也与 n 同阶，这里取 q = 2 * 10**5，保证有大于 1e5+1 的询问
    q = 2 * 10**5

    # 生成一个长度为 n 的序列 A
    # 这里使用 1..n 的一个乱序排列作为测试数据
    A = list(range(1, n + 1))
    random.shuffle(A)

    # 生成 q 个询问，每个询问是一个正整数
    # 部分在 [1, 10**5+1]，部分远大于 10**5+1
    Q = []
    limit = 10 ** 5 + 1
    for _ in range(q):
        if random.random() < 0.5:
            # 一半概率在前 1e5+1 内
            Q.append(random.randint(1, limit))
        else:
            # 一半概率取更大的值
            Q.append(random.randint(limit + 1, limit + 10 ** 9))

    # 2. 原始逻辑
    A_deque = deque(A)
    ANS = [0]  # 占位，使 ANS[q] 与题目下标对齐

    for _ in range(10 ** 5 + 1):
        x = A_deque.popleft()
        y = A_deque.popleft()

        ANS.append((x, y))

        if x > y:
            A_deque.appendleft(x)
            A_deque.append(y)
        else:
            A_deque.appendleft(y)
            A_deque.append(x)

    ANS0 = A_deque[0]
    B = list(A_deque)[1:]  # 长度 n-1 的循环部分

    # 3. 输出答案（保持与原代码输出行为一致）
    for qi in Q:
        if qi <= 10 ** 5 + 1:
            x, y = ANS[qi]
            print(x, y)
        else:
            idx = (qi - 10 ** 5 - 2) % (n - 1)
            print(ANS0, B[idx])


if __name__ == "__main__":
    # 示例：调用 main(n)，可根据需要修改 n
    main(5)