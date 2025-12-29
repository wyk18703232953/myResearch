from __future__ import division
from math import ceil

def main(n):
    # 生成测试数据：令 k 与 n 相关，这里简单设定为 k = max(1, n // 2)
    # 可根据需要调整生成规则
    k = max(1, n // 2)

    red = 2 * n
    green = 5 * n
    blue = 8 * n

    need = int(ceil(red / k)) + int(ceil(green / k)) + int(ceil(blue / k))
    print(need)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的取值
    main(10)