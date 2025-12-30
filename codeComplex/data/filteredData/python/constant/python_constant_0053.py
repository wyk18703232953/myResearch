import itertools
import random

def generate_47_arr():
    arr = []
    for digits in range(1, 4):
        arr += itertools.product("47", repeat=digits)
    for i in range(len(arr)):
        arr[i] = int("".join(list(arr[i])))
    arr.append(4444444444)
    return arr

def is_good(num, good_num_arr):
    for element in good_num_arr:
        if num % element == 0:
            return True
    return False

def main(n):
    """
    n: 生成的测试数据数量（规模）
    逻辑：生成 n 个正整数，对每个数判断是否能被“好数”整除，输出 YES/NO。
    """
    good_num_arr = generate_47_arr()

    # 根据 n 生成 n 个测试数据，这里简单生成 1 到 10^9 范围内的随机数
    random.seed(0)
    test_numbers = [random.randint(1, 10**9) for _ in range(n)]

    for num in test_numbers:
        if is_good(num, good_num_arr):
            print("YES")
        else:
            print("NO")

# 示例调用（提交到评测系统时可删除或注释掉）
if __name__ == "__main__":
    main(5)