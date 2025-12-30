from collections import defaultdict
import random

def main(n: int) -> int:
    # 生成测试数据：随机整数数组 a，取值范围可根据需要调整
    # 这里设为 1 到 10^9
    a = [random.randint(1, 10**9) for _ in range(n)]

    d = defaultdict(int)
    cnt = 0

    for i in range(n):
        d[a[i]] += 1

    for i in range(n):
        f = 0
        for j in range(1, 31):
            p = 2 ** j - a[i]
            if p <= 0:
                continue
            if p != a[i]:
                if d[p] >= 1:
                    f = 1
            else:
                if d[p] >= 2:
                    f = 1
        if not f:
            cnt += 1

    # 保持原逻辑的输出行为：打印并返回结果
    print(cnt)
    return cnt

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)