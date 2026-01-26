def size_of_group(i: int) -> int:
    # number of digits contributed by all i-digit numbers
    return 9 * (10 ** (i - 1)) * i

def find_group(k: int, i: int = 1):
    # find the digit-length group where the k-th digit lies
    diff = k - size_of_group(i)
    if diff <= 0:
        return k, i
    return find_group(diff, i + 1)

def get_number(k: int, g: int) -> str:
    # find the digit at position k (0-based) within group g
    start = 10 ** (g - 1)
    num = start + k // g
    return str(num)[k % g]

def get_sequence_number(num: int) -> str:
    # main logic from original codeforces problem 1177B
    k_prim, g_prim = find_group(num)
    return get_number(k_prim - 1, g_prim)

def main(n: int):
    """
    根据规模 n 生成测试数据并打印结果。
    这里将测试数据设为 1..n 的查询，每个查询是
    序列中的第 i 个数字，依次打印。
    """
    for i in range(1, n + 1):
        # print(get_sequence_number(i))
        pass

# 示例：如果需要直接运行，可取消以下注释
# if __name__ == "__main__":
#     main(10)