import random

def replace(arr):
    if arr == [1] * len(arr):
        arr[-1] = 2
        print(*sorted(arr))
        return ""
    arr[arr.index(max(arr))] = 1
    print(*sorted(arr))
    return ""

def main(n):
    # 生成长度为 n 的测试数据，元素取值范围 [1, 5]
    lst = [random.randint(1, 5) for _ in range(n)]
    return replace(lst)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)