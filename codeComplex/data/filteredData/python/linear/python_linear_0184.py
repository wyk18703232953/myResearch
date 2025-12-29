import random

def get_answer(arr):
    current_sum = 0
    total = sum(arr)
    for index, val in enumerate(arr):
        current_sum += val
        if current_sum >= total / 2:
            return index + 1

def main(n):
    # 生成规模为 n 的测试数据，这里生成 1~100 的随机整数
    values = [random.randint(1, 100) for _ in range(n)]
    result = get_answer(values)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)