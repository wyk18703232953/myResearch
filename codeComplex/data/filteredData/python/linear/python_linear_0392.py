# by the authority of GOD     author: manhar singh sachdev #

def some_random_function():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function5():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def main(n):
    # 1. 预处理幂数组（与原逻辑一致）
    mod = 998244353
    powe = [1]
    for _ in range(10**6):
        powe.append((powe[-1] * 2) % mod)

    # 2. 根据 n 生成测试数据（示例：生成从 1 到 n 的数组）
    # 可以根据需要自行调整生成策略
    a = list(range(1, n + 1))

    # 3. 原 main 的核心逻辑
    ans = (a[0] * powe[n - 1]) % mod
    dp = a[0]
    dp1 = 0

    for i in range(1, n):
        if i == 1:
            dp = (dp + a[i]) % mod
        else:
            dp = (dp * 2 + a[i] - dp1) % mod
        ans = (ans + powe[n - i - 1] * dp) % mod
        dp1 = a[i]

    print(ans)
    return ans


def some_random_function1():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function2():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function3():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function4():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function6():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function7():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


def some_random_function8():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    print(i_dont_know)
    print(why_am_i_writing_this)


if __name__ == '__main__':
    # 示例调用：规模为 5
    main(5)