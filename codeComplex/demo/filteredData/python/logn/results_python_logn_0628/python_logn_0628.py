def AP_Term(n):
    return (n * (1 + n)) // 2

def main(n):
    # 根据规模 n 生成测试数据:
    # act 取为 n，cleft 取为 1..AP_Term(n) 中的某个值
    act = n
    # 这里简单选取 cleft 为 AP_Term(n) // 2（既不是极端值，又保证规模随 n 变化）
    cleft = AP_Term(act) // 2

    if cleft != AP_Term(act):
        low = 1
        high = act
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            candy_in = AP_Term(mid)
            moves_left = (act - mid)
            if cleft == (candy_in - moves_left):
                ans = moves_left
                break
            elif cleft > (candy_in - moves_left):
                low = mid + 1

            else:
                high = mid - 1
        # print(ans)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)