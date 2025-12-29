import random
import time

# 原程序逻辑是交互式的，通过多次询问比较两个隐藏数 a,b 的大小关系
# 这里我们在 main(n) 中自行生成 a,b，并用内部函数 query(a,b) 模拟交互返回结果：
#   返回 -1 如果 a < b
#   返回  0 如果 a == b
#   返回  1 如果 a > b
#
# 原程序中所有 input() 被替换为对 query 的调用，print('? ...') 去掉，仅保留最终结果。

def main(n: int):
    # 使用 n 控制生成数据的规模：这里简单地在 [0, 2^n - 1] 中生成两个数
    # 若 n > 30，则逻辑上原程序只用到 30 bit，所以我们限制到 30
    max_bits = min(n, 30)
    if max_bits <= 0:
        max_bits = 1

    # 生成隐藏数 a, b
    rand = random.Random(int(time.time()))
    max_val = (1 << max_bits) - 1
    a = rand.randint(0, max_val)
    b = rand.randint(0, max_val)

    # 用于模拟交互比较
    def query(x, y):
        # 原题是比较 (a xor x) 与 (b xor y)
        ax = a ^ x
        by = b ^ y
        if ax < by:
            return -1
        elif ax > by:
            return 1
        else:
            return 0

    # 以下为原程序核心逻辑，只是把交互改为 query 调用
    bb = rand.randint(0, (1 << 30) - 1)

    hat1 = 0
    hat2 = 0
    lastresult = None
    for i in range(29, -1, -1):
        g1 = hat1 + (1 << i)
        g2 = hat2 + (1 << i)

        if lastresult is None:
            t1 = query(hat1 ^ bb, hat2)
        else:
            t1 = lastresult

        if t1 != 0:
            t2 = query(g1 ^ bb, g2)
            if t1 != t2:
                if t1 == 1:
                    hat1 += (1 << i)
                else:
                    hat2 += (1 << i)
                lastresult = None
                continue

        lastresult = t1
        t3 = query(g1 ^ bb, hat2)
        if t3 == 1:
            pass
        else:
            hat1 += (1 << i)
            hat2 += (1 << i)

    # 原代码输出的是 (hat1 ^ bb) % 2^30, hat2
    x = (hat1 ^ bb) % (1 << 30)
    y = hat2

    # 为了验证算法正确性，这里也输出真实 a,b，可按需要保留/删除
    print("hidden a,b:", a, b)
    print("recovered:", x, y)

if __name__ == "__main__":
    # 示例：规模 n = 30
    main(30)