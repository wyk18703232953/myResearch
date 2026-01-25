from collections import Counter

def generate_strings(n):
    # 生成两个长度为 n 的字符串序列，完全由 n 决定
    # 第一组：s0_i = "A_" + str(i % (n // 2 + 1))
    # 第二组：s1_i = "A_" + str(i % (n // 2 + 1)) 或 "B_" + str(i % (n // 3 + 1))
    first = ["A_" + str(i % (n // 2 + 1)) for i in range(n)]
    second = []
    split_point = n // 3
    for i in range(n):
        if i < split_point:
            second.append("A_" + str(i % (n // 2 + 1)))
        else:
            second.append("B_" + str(i % (n // 3 + 1)))
    return first, second

def main(n):
    a = Counter()
    b = Counter()
    first, second = generate_strings(n)
    for s in first:
        a[s] += 1
    for s in second:
        b[s] += 1
    ans = 0
    for key in b:
        ans += max(b[key] - a[key], 0)
    print(ans)

if __name__ == "__main__":
    main(10)