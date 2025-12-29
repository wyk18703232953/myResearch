import random

def main(n: int):
    # 生成测试数据：长度为 n 的随机整数数组
    # 元素范围可根据需要调整
    arr = [random.randint(0, 100) for _ in range(n)]

    li = arr[:]
    li.sort()
    c = 0
    for i in range(n):
        if arr[i] != li[i]:
            c += 1
        if c > 2:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)