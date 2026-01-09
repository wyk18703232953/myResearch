MOD = 1000000007

def main(n):
    # 1. 生成规模为 n 的测试数据
    # 设定 q 的规模，这里简单设置为 n（可按需调整）
    q = n

    # 生成一个长度为 n 的01串，简单用循环构造（也可用随机数）
    # 例如：周期性 "01" 重复
    x = ''.join('01'[i % 2] for i in range(n))

    # 生成 q 个查询，简单构造为 [1,1], [1,2], ..., [1,min(n,q)]
    query_list = []
    for i in range(1, q + 1):
        l = 1
        r = min(i, n)
        query_list.append((l, r))

    # 2. 原逻辑计算
    sum_list = [0]  # 前缀和，1-based
    for i, deliciousness in enumerate(x):
        sum_list.append(int(deliciousness) + sum_list[i])

    enjoyment_list = [0]
    for i in range(n):
        enjoyment_list.append((enjoyment_list[i] * 2 + 1) % MOD)

    # 3. 处理查询并输出
    for l, r in query_list:
        banhmi_count = r - l + 1
        delicious_count = sum_list[r] - sum_list[l - 1]
        non_delicious_count = banhmi_count - delicious_count
        if delicious_count == 0:
            enjoyment = 0

        else:
            enjoyment = enjoyment_list[delicious_count]
            enjoyment += (enjoyment_list[banhmi_count]
                          - enjoyment_list[delicious_count]
                          - enjoyment_list[non_delicious_count])
            enjoyment %= MOD
        # print(enjoyment)
        pass
if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)