#!/usr/bin/env python3
import random

def main(n):
    # 生成测试数据：长度为 n 的数组，每个元素在 [0, n//2] 范围内
    # 保证数组长度为偶数，这样可以成对匹配
    if n % 2 == 1:
        n += 1
    max_val = max(1, n // 2)
    a = [random.randint(0, max_val) for _ in range(n)]

    # 原逻辑
    r = 0
    while a:
        c = a[0]
        del a[0]
        for i in range(len(a)):
            if c == a[i]:
                break
        del a[i]
        r += i
    print(r)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)