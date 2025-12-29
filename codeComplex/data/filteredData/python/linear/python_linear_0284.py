import random

op = [0] * 1000000
cl = [0] * 1000000

def fun(s):
    v = []
    for ch in s:
        if ch == '(':
            v.append(ch)
        elif v and v[-1] == '(':
            v.pop()
        else:
            v.append(')')
    l = len(v)
    if l == 0:
        op[0] += 1
        cl[0] += 1
    elif v[0] == v[-1]:
        if v[0] == '(':
            op[l] += 1
        else:
            cl[l] += 1

def generate_test_string(length):
    return ''.join(random.choice('()') for _ in range(length))

def main(n):
    # 清零全局数组
    for i in range(1000000):
        op[i] = 0
        cl[i] = 0

    # 生成 n 个测试串，长度可根据需要调整，这里设为 1~20 的随机长度
    for _ in range(n):
        length = random.randint(1, 20)
        s = generate_test_string(length)
        fun(s)

    ans = 0
    for i in range(1000000):
        ans += op[i] * cl[i]

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10) 进行规模为 10 的测试
    main(10)