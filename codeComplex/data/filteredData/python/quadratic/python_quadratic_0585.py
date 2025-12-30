import random

def main(n):
    # 生成测试数据：构造 t 个测试用例
    # 这里让 t 与 n 相同，每个用例的字符串长度也为 n
    # 你可以根据需要修改生成策略
    t = n
    print(f"t = {t}")
    for _ in range(t):
        # 生成 k：1 <= k <= n
        k = random.randint(1, n)
        # 生成长度为 n 的字符串，只包含 'R', 'G', 'B'
        s = ''.join(random.choice('RGB') for _ in range(n))

        print(f"n = {n}, k = {k}, s = {s}")

        mini = n
        # 三种起始模式
        for base in ("RGB", "GBR", "BRG"):
            test = base * (k // 3 + 5)  # 保证长度足够
            for i in range(n - k + 1):
                count = 0
                # 统计窗口 [i, i+k) 内与模式的不同字符数
                for j in range(k):
                    if s[i + j] != test[j]:
                        count += 1
                if count < mini:
                    mini = count

        print(f"answer = {mini}")