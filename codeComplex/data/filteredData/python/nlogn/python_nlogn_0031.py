import random

def secondorder(arr, size):
    arr.sort()
    return arr[1]

def main(n):
    # 生成测试数据：长度为 n 的随机整数数组（允许重复）
    # 元素范围可按需调整，这里设为 1 到 100
    raw_nums = [random.randint(1, 100) for _ in range(n)]

    # 构造去重后的列表，保留出现顺序
    unique_list = []
    for v in raw_nums:
        if v not in unique_list:
            unique_list.append(v)

    # 模拟原逻辑
    if len(unique_list) == 1:
        print("NO")
    else:
        print(secondorder(unique_list, n))

    # 如需观察生成的测试数据，可取消下面注释
    # print("raw:", raw_nums)
    # print("unique:", unique_list)

if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)