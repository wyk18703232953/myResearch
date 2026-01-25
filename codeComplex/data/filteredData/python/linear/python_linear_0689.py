import math

def f(n, k):
    if k == 1:
        return (n * (n + 1)) // 2
    a = math.floor(math.log(n, k))
    b = sum(k ** i for i in range(a + 1))
    c = sum((i + 1) * k ** i for i in range(a + 1))
    if n < b:
        return c - (b - n) * (a + 1)
    else:
        return c + (n - b) * (a + 2)

def main(n):
    # 由 n 确定性生成原程序的两个输入: 原来的 n 和 s
    # 这里使用:
    #   original_n = max(1, n)
    #   s 在 [1, (original_n*(original_n+1))//2] 区间内变化
    original_n = max(1, n)
    max_sum = (original_n * (original_n + 1)) // 2
    # 为了让不同 n 有不同分布, 使用简单算术构造 s
    # 当 max_sum>0 时, 让 s 在 [1, max_sum] 上循环
    if max_sum == 0:
        s = 0
    else:
        s = (n % max_sum) + 1

    n_val = original_n

    if s == (n_val * (n_val + 1)) // 2:
        print("Yes")
        a = [str(i + 1) for i in range(n_val - 1)]
        print(" ".join(a))
    elif s > (n_val * (n_val + 1)) // 2:
        print("No")
    elif s < 2 * n_val - 1:
        print("No")
    else:
        mini = 1
        maxi = n_val - 1
        curr = 1
        while True:
            a_val, b_val = f(n_val, curr), f(n_val, curr + 1)
            if b_val > s:
                mini = curr + 1
                curr = math.ceil((curr + maxi) / 2)
            elif a_val <= s:
                maxi = curr - 1
                curr = (curr + mini) // 2
            else:
                opt = curr + 1
                break
        depths = [0, 1] + [0] * (n_val - 1)
        ins = 1
        ind = 2
        while True:
            a_depth = min(opt ** (ind - 1), n_val - ins)
            depths[ind] = a_depth
            ind += 1
            ins += a_depth
            if ins == n_val:
                break
        left = s - b_val
        far = ind - 1
        bulk = ind - 1
        if depths[bulk] == 1:
            bulk -= 1
        while left > 0:
            if far + 1 - bulk <= left:
                far += 1
                left -= far - bulk
                depths[far] += 1
                depths[bulk] -= 1
                if depths[bulk] == 1:
                    bulk -= 1
            else:
                depths[bulk] -= 1
                depths[bulk + left] += 1
                left = 0
        verts = [None] * far
        sumi = 0
        for i in range(far):
            verts[i] = list(range(sumi + 1, sumi + 1 + depths[i + 1]))
            sumi += depths[i + 1]
        out = ""
        for i in range(1, far):
            for j in range(len(verts[i])):
                out += str(verts[i - 1][j // opt]) + " "
        print("Yes")
        print(out)

if __name__ == "__main__":
    # 示例调用: 可调整 n 观察规模变化
    main(10)