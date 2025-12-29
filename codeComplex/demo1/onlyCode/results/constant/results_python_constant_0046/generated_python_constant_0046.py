def main(n: int) -> None:
    # 这里的“根据 n 生成测试数据”理解为：n 由外部传入，函数内部不再调用 input()
    # 若需要，可在外部根据 n 的范围随机/按需生成多个样例，再循环调用 main
    
    l = [4, 7, 47, 74, 444, 447, 474, 477, 747, 744, 774, 777]

    for i in l:
        if n % i == 0:
            print('YES')
            break
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：这里简单地用 n = 100 作为测试数据
    # 实际使用时可根据需要生成不同的 n 再调用 main(n)
    test_n = 100
    main(test_n)