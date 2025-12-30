def sum_from1(k):
    return (k * (k + 1)) // 2

def sum_of_subtraction(p, k):
    if p <= 1:
        return sum_from1(k)
    else:
        return sum_from1(k) - sum_from1(p - 1)

def main(n):
    # 根据规模 n 生成测试数据 (n, k)
    # 这里设定一个简单策略：k = n // 2 + 1（确保有一定规模关系）
    # 如需其他测试策略，可自行修改此处。
    k = max(1, n // 2 + 1)

    # 以下为原始逻辑
    if n == 1:
        print(0)
    elif n <= k:
        print(1)
    else:
        n -= 1
        k -= 1
        if n > sum_from1(k):
            print(-1)
        else:
            s = 1
            e = k

            while s < e:
                mid = (s + e) // 2
                r = sum_of_subtraction(mid, k)

                if r == n:
                    print(k - mid + 1)
                    break
                elif r > n:
                    s = mid + 1
                else:
                    e = mid
            else:
                print(k - s + 2)


# 示例调用
if __name__ == "__main__":
    # 使用不同的 n 测试时，只需修改这里的参数
    main(10)