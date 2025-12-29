from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial

def main(n: int):
    # 生成测试数据：k 为 1 到 n 之间的某个正整数，这里简单设为 n//2+1（保证 >=1）
    if n <= 0:
        return 0  # 规模为非正时，返回0或按需处理
    k = n // 2 + 1

    result = (
        (n * 2 + k - 1) // k +
        (n * 5 + k - 1) // k +
        (n * 8 + k - 1) // k
    )

    print(result)
    return result

if __name__ == "__main__":
    # 示例：可自行修改 n 的值做测试
    main(10)