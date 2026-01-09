def some_random_function():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function5():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function1():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function2():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function3():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function4():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function6():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function7():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def some_random_function8():
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x * x
    # print(i_dont_know)
    pass
    # print(why_am_i_writing_this)
    pass


def main(n):
    mod = 998244353
    # Precompute powers of 2 up to n (scaled from original 10**6 to n for scalability)
    powe = [1]
    for _ in range(max(n, 1)):
        powe.append((powe[-1] * 2) % mod)

    # Deterministically generate input array a of length n
    # Example pattern: a[i] = (i * (i + 1)) % mod
    if n <= 0:
        # print(0)
        pass
        return

    a = [(i * (i + 1)) % mod for i in range(n)]

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
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10**5)