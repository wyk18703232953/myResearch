import random

def val(s):
    ans = ((int(s.split('+')[0][1:]) + int(s.split('+')[1].split(')')[0])) / int(s.split('/')[1]))
    return ans

def main(n):
    # 生成 n 条形如 "(a+b)/c" 的测试数据
    # 为避免除零，c 从 1 开始取值
    expressions = []
    for _ in range(n):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(1, 10)
        expr = f"({a}+{b})/{c}"
        expressions.append(expr)

    s = []
    f = {}
    for ss in expressions:
        v = val(ss)
        s.append(v)
        if v not in f:
            f[v] = 1
        else:
            f[v] += 1

    for v in s:
        print(f[v], end=" ")
    print()

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)