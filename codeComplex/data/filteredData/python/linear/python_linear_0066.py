def main(n):
    s = n * 2
    ans = s
    s_i = s
    pairs = [(i + 1, (i * 3) % (s + 5) + 1) for i in range(n)]
    for f_i, t_i in pairs:
        if t_i > (s_i - f_i):
            delta = t_i - (s_i - f_i)
            ans += delta
            s_i += delta
    return ans

if __name__ == "__main__":
    for test_n in [1, 5, 10, 50]:
        # print(test_n, main(test_n))
        pass