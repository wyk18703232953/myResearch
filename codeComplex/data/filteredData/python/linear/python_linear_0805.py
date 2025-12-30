from collections import deque
import random

def main(n: int) -> int:
    """
    n: 规模，用于生成测试数据
    返回：原程序的输出（oper）
    """
    # 根据 n 生成测试数据
    # 这里约定：
    #   m = n
    #   k 在 [1, max(1, n//3)] 中随机取值
    #   a 为长度为 m 的递增正整数序列，值在 [1, 10*n] 内
    m = n
    k = max(1, n // 3)  # 可根据需要修改生成规则
    k = random.randint(1, k)

    # 生成递增数组 a
    a = []
    cur = 0
    for _ in range(m):
        cur += random.randint(1, max(1, 10))  # 保证递增
        a.append(cur)

    # 将原逻辑封装
    dq = deque(a)
    oper = 0
    rem = 0
    while dq:
        x = dq.popleft()
        pg = (x - 1 - rem) // k
        lrem = 1
        while dq and (dq[0] - 1 - rem) // k == pg:
            dq.popleft()
            lrem += 1
        rem += lrem
        oper += 1

    return oper

if __name__ == "__main__":
    # 示例：调用 main(10)，可以根据需要修改 n
    result = main(10)
    print(result)