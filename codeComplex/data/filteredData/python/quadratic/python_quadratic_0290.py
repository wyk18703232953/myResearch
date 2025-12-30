import random

def main(n):
    # 生成测试数据：长度为 2*n 的整数数组
    # 这里生成 [1..n] 每个出现两次并打乱顺序，保证逻辑可用
    a = list(range(1, n + 1)) * 2
    random.shuffle(a)

    ans = 0
    pos = 2 * n - 2
    # 拷贝一份数组用于操作，避免外部引用被修改
    arr = a[:]

    for _ in range(n):
        x = arr[-1]
        arr.pop(-1)
        y = arr.index(x)
        ans += pos - y
        pos -= 2
        arr.pop(y)

    # 输出与原程序一致的结果（只输出答案）
    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的默认值
    main(3)