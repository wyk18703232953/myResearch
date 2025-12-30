import random

def main(n: int):
    # 这里根据 n 生成测试数据，如果需要可替换为其它生成逻辑
    # 但当前算法本身只依赖于 n，不需要额外数据。
    # 为符合要求，示例生成一个与 n 相关的随机列表，但不参与原逻辑计算。
    test_data = [random.randint(1, n) for _ in range(max(1, min(n, 10)))]

    if n == 3:
        print('1 1 3')
    else:
        done = 0
        arr = []
        for i in range(30, -1, -1):
            arr.extend([2**i] * (n // (2**i) - done))
            done += n // (2**i) - done
            if done == 1:
                k = i

        arr[0] = max(arr[0], (n // 2**(k - 1)) * 2**(k - 1))

        arr.reverse()
        print(' '.join(map(str, arr)))


if __name__ == "__main__":
    # 示例调用：可以自行修改 n 的值进行测试
    main(10)