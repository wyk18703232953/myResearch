import math
import sys

def main(n):
    r = 0
    t = 1
    for i in range(n - 1):
        r += t * 2
        t += 2
    result = r + t
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)