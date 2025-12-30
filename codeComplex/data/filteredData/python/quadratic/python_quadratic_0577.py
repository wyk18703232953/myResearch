import random

def main(n):
    # 生成测试数据：
    # q：查询次数，约为 n（也可以按需要自行调整规则）
    # 对于每个查询：
    #   - 随机生成 1 <= k <= n_i 的窗口大小
    #   - 随机生成长度为 n_i 的字符串 s（只含 R/G/B）
    q = max(1, n)  # 至少一个测试
    print(q)
    for _ in range(q):
        # 为了多样性，可以让每个测试用例的长度在 [1, n] 之间波动
        length = random.randint(1, n)
        k = random.randint(1, length)
        s = ''.join(random.choice('RGB') for _ in range(length))

        # 输出生成的测试数据（可选，如果只想要答案可以去掉这三行）
        print(length, k)
        print(s)

        # 以下是原逻辑的封装（对每个用例计算答案）
        min_ans = 10 ** 9
        for i in range(length - k + 1):
            count1 = 0
            count2 = 0
            count3 = 0
            for j in range(k):
                pos = i + j
                r = s[pos]
                mod = pos % 3

                if mod == 0:
                    if r != "R":
                        count1 += 1
                    if r != "G":
                        count2 += 1
                    if r != "B":
                        count3 += 1
                elif mod == 1:
                    if r != "G":
                        count1 += 1
                    if r != "B":
                        count2 += 1
                    if r != "R":
                        count3 += 1
                else:  # mod == 2
                    if r != "B":
                        count1 += 1
                    if r != "R":
                        count2 += 1
                    if r != "G":
                        count3 += 1

            min_ans = min(min_ans, count1, count2, count3)

        print(min_ans)


# 示例：调用 main(10) 生成规模为 10 的测试数据并计算答案
# main(10)