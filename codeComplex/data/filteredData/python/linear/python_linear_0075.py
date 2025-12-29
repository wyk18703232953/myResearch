import random

def solve(a, b):
    m = len(a)
    n = len(b)
    p_b = [0]
    for x in b:
        p_b.append(p_b[-1] + int(x))
    s = 0
    span = n - m + 1
    for i in range(m):
        ones_in_window = p_b[span + i] - p_b[i]
        if a[i] == '0':
            s += ones_in_window
        else:
            s += span - ones_in_window
    return s

def main(n):
    # 生成测试数据：a 为长度 n，b 为长度 2n（保证 b 长度 >= a）
    m = n
    len_b = 2 * n
    a = ''.join(random.choice('01') for _ in range(m))
    b = ''.join(random.choice('01') for _ in range(len_b))

    ans = solve(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例：用 n = 5 运行
    main(5)