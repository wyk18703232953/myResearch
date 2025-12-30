import random

def main(n):
    # 生成长度固定为 14 的测试数据，元素值与规模 n 相关
    # 这里设定每个元素在 [0, n] 范围内随机生成
    a = [random.randint(0, n) for _ in range(14)]

    h = 0
    for idx in range(14):
        b = a[:]
        if idx == 13:
            j = 0
        else:
            j = idx + 1
        if a[idx] > 0:
            c = 0
            t = b[idx] % 14
            x = b[idx] // 14
            b[idx] = 0
            for k in range(14):
                b[k] += x
            while t > 0:
                b[j] += 1
                j += 1
                if j == 14:
                    j = 0
                t -= 1
            for k in range(14):
                if b[k] % 2 == 0:
                    c += b[k]
            if c > h:
                h = c
    print(h)

# 示例调用
if __name__ == "__main__":
    main(100)