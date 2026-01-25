n = 0
a = 0
b = 0
c = 0
t = 0

def generate_inputs(n):
    # 映射：n 为列表长度，同时决定 t 的上界
    # 保证 t 至少为 1，且不小于列表中元素的最大值
    global a, b, c, t
    a = 2
    b = 1
    c = 3
    t = max(1, n + 1)
    l = [(i % t) for i in range(1, n + 1)]
    return n, a, b, c, t, l

def core_logic(n, a, b, c, t, l):
    f = [0] * 1001
    for i in l:
        if 0 <= i < len(f):
            f[i] += 1
    tmp = 0
    for i in range(1, t):
        if i < len(f):
            tmp += (t - i) * f[i]
    tmp = n * a + tmp * c - tmp * b
    return max(n * a, tmp)

def main(n):
    n_gen, a_gen, b_gen, c_gen, t_gen, l_gen = generate_inputs(n)
    result = core_logic(n_gen, a_gen, b_gen, c_gen, t_gen, l_gen)
    print(result)

if __name__ == "__main__":
    main(10)