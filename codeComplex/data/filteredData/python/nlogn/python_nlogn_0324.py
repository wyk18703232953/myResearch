import random

def main(n: int):
    # 生成测试数据：nums 为 1..n 的随机排列
    nums = list(range(1, n + 1))
    random.shuffle(nums)

    swaps = 0
    visited = set()
    for index in range(n):
        if index in visited:
            continue
        visited.add(index)
        length = 0
        value = nums[index]
        while value != index + 1:
            visited.add(value - 1)
            value = nums[value - 1]
            length += 1
        swaps += length

    if (3 * n - swaps) % 2:
        print("Um_nik")
    else:
        print("Petr")


if __name__ == "__main__":
    # 示例调用，可修改 n 测试不同规模
    main(10)