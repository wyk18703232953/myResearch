import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数序列
    # 构造时保证只有一个数与其他数奇偶性不同，以符合原题设定
    if n < 3:
        # 至少需要 3 个数才比较合理，这里简单兜底
        n = 3

    # 随机决定大多数是偶数还是奇数
    majority_is_even = random.choice([True, False])

    # 生成 n-1 个同奇偶性的数
    arr = []
    for _ in range(n - 1):
        if majority_is_even:
            # 生成偶数
            val = random.randrange(-1000, 1001) * 2
        else:
            # 生成奇数
            val = random.randrange(-1000, 1001) * 2 + 1
        arr.append(val)

    # 生成唯一一个异奇偶的数并插入随机位置
    if majority_is_even:
        odd_val = random.randrange(-1000, 1001) * 2 + 1
        special_val = odd_val
    else:
        even_val = random.randrange(-1000, 1001) * 2
        special_val = even_val

    special_pos = random.randrange(0, n)
    arr.insert(special_pos, special_val)

    # 以下为原题逻辑：找出唯一与其他数奇偶性不同的数的位置（1-based）
    odd = even = 0
    oddIndex = evenIndex = 0
    counter = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
            evenIndex = counter
        else:
            odd += 1
            oddIndex = counter
        counter += 1

    ans = evenIndex + 1 if even == 1 else oddIndex + 1
    print(ans)


# 示例：需要时可以手动调用 main
# main(10)