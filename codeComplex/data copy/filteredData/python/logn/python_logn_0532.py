import math

def countDigit(n):
    return math.floor(math.log(n, 10) + 1)

def core_algorithm(n):
    count = countDigit(n)
    if count == 1:
        return n

    else:
        low = 1
        high = 9
        sum_list = []
        digit = 0
        sum_list.append(0)
        sum_list.append(9)
        for i in range(2, 16):
            low = low * 10
            high = high * 10 + 9
            sum_list.append((high - low + 1) * i + sum_list[i - 1])

            if n < sum_list[i]:
                digit = i
                break
        x = n - sum_list[digit - 1]
        q = x // digit
        r = x % digit
        low = int(math.pow(10, digit - 1))
        low = low + q - 1
        if r == 0:
            return int(low % 10)

        else:
            n_val = low + 1
            stringnum = str(n_val)
            return int(stringnum[r - 1])

def main(n):
    # 将 n 作为“输入规模”，构造确定性的测试数据
    # 这里构造 n 个查询，每个查询的值是 1 到 n 的某种确定性映射
    # 如使用 i*i + 1 再限制在一定范围内
    if n <= 0:
        return

    # 为了与原算法的适用范围匹配，构造较大的查询值
    # 确保不会越界 sum_list 预设的 16 位范围
    # 这里选择查询值在 [1, 10**15] 范围内
    max_query = 10 ** 15
    results = []
    for i in range(1, n + 1):
        # 确定性映射：i^2 + i，之后按范围取模并加 1，避免为 0
        q = (i * i + i) % max_query + 1
        results.append(core_algorithm(q))

    # 输出所有结果，保证有可观察的运行行为
    # 这里简单逐行打印
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以做规模化实验
    main(1000)