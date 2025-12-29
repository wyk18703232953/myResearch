import random

def main(n):
    # 生成规模为 n 的测试数据 a
    # 这里生成 [-10^9, 10^9] 范围内的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑封装为内部函数
    def f(a):
        b = [a[0]]
        for e in a[1:]:
            if b != []:
                if e == b[-1] or abs(e - b[-1]) % 2 == 0:
                    b.pop()
                else:
                    b.append(e)
            else:
                b.append(e)

        for i in range(1, len(b)):
            if abs(b[i] - b[i - 1]) % 2:
                print('NO')
                return

        print('YES')

    if n == 0:
        # 若规模为 0，可根据需要定义行为，这里直接输出 YES
        print("YES")
        return

    f(a)


# 示例：直接运行时可给一个默认规模
if __name__ == "__main__":
    main(5)