def main(n: int):
    # 生成测试数据：这里假设 v 为 1 到 n 之间的某个值
    # 可按需要修改生成方式
    v = max(1, n // 2)  # 示例：取 v 为 n 的一半（向下取整，至少为 1）

    answer = 0
    n -= 1
    if n <= v:
        result = n
    else:
        answer = v
        for i in range(1, n - v + 1):
            answer += (i + 1)
        result = answer

    print(result)


if __name__ == "__main__":
    # 示例：运行 main，规模 n 可按需修改
    main(10)