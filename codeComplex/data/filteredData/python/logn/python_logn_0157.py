def sum_arith(k, r):
    # 原sum函数：求从 r-k+1 到 r 的等差数列和
    return k * (2 * r - (k - 1)) // 2

def function(total, l, r):
    left = l
    right = r

    while left <= right:
        mid = (right + left) // 2
        result = sum_arith(r - mid + 1, r)
        if result == total:
            return r - mid + 1
        elif result > total:
            left = mid + 1

        else:
            if sum_arith(r - mid + 2, r) > total:
                return r - mid + 2

            else:
                right = mid - 1
    return -1

def main(n):
    """
    将原来的两参数 (n, m) 问题改为由单一规模参数 n 自动生成测试数据。
    这里的策略是：
      - 令原始 n_input = n
      - 令原始 m_input = n  (可以根据需要修改生成策略)
    然后执行原程序逻辑并返回结果。
    """
    # 生成测试数据（原程序中读取的 n, m）
    n_input = n
    m_input = n

    # 对应原代码逻辑
    n_val = n_input - 1
    m_val = m_input - 1

    if n_val == 0:
        result = 0
    elif sum_arith(m_val, m_val) < n_val:
        result = -1
    elif m_val < n_val:
        result = function(n_val, 1, m_val)

    else:
        result = 1

    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)