import random

def main(n: int):
    dict1 = {}
    dict2 = {}

    # 根据 n 生成测试数据：
    # 生成形如 "(a+b)/c" 的表达式，其中 a,b,c 为随机整数且 c != 0
    expressions = []
    for _ in range(n):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = 0
        while c == 0:
            c = random.randint(-10, 10)
        expr = f"({a}+{b})/{c}"
        expressions.append(expr)

    # 原逻辑
    for i in range(n):
        s = expressions[i]
        s = s.split('/')
        c = int(s[1])
        s = s[0].strip('(').strip(')').split('+')
        a = int(s[0])
        b = int(s[1])
        ans = (a + b) / c
        try:
            dict2[ans] += 1
        except KeyError:
            dict2[ans] = 1
        dict1[i] = ans

    for i in range(n):
        print(dict2[dict1[i]], end=' ')

if __name__ == "__main__":
    # 示例调用
    main(5)