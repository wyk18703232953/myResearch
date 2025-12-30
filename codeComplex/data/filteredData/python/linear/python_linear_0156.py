import random

def main(n):
    arr = []
    d = {}

    # 根据 n 生成测试数据
    # 生成形如 "(a+b)/c" 的字符串，并按原程序逻辑解析
    for _ in range(n):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        # 避免除零
        c = random.randint(1, 20)
        s = f"({a}+{b})/{c}"

        # 原始解析逻辑
        a_, b_, c_ = tuple(map(int, s.replace("(", "")
                                     .replace(")", "")
                                     .replace("/", ".")
                                     .replace("+", ".")
                                     .split(".")))
        x = (a_ + b_) / c_
        arr.append(x)
        if x not in d:
            d[x] = 0
        d[x] += 1

    # 输出结果
    for i in arr:
        print(d[i], end=" ")

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)