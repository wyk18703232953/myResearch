import math
import random

def main(n: int):
    # 1. 根据 n 生成测试数据（本题逻辑只需要 n，直接使用传入的 n）
    # 若需要更复杂的测试数据，可在此扩展生成逻辑
    
    # 2. 原程序逻辑封装
    x = int(n ** 0.5)
    i = 0
    y = n
    ans = []
    while i < n:
        arr = []
        for _ in range(x):
            if y == 0:
                break
            arr.append(y)
            y -= 1
            i += 1
            if y == 0:
                break
        arr.reverse()
        ans.extend(arr)
    
    print(*ans)


# 示例：调用 main(10) 测试
if __name__ == "__main__":
    main(10)