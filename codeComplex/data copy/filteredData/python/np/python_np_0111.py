def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main(n):
    # 生成长度为 n 的 original，随机由 '+' 和 '-' 组成，
    # 这里简单生成一半 '+' 一半 '-'（若 n 为奇数，多出的用 '+'）
    plus_count = (n + 1) // 2
    minus_count = n - plus_count
    original = '+' * plus_count + '-' * minus_count

    # 生成长度为 n 的 received，前 n//3 个 '+', 中间 n//3 个 '-', 剩余用 '?'
    part = n // 3
    received = '+' * part + '-' * part + '?' * (n - 2 * part)

    originalNum = original.count('+') - original.count('-')
    receivedNum = received.count('+') - received.count('-')

    variance = received.count('?')
    difference = abs(originalNum - receivedNum)

    if variance == 0:
        if difference == 0:
            # print(1.0)
            pass

        else:
            # print(0.0)
            pass
    elif difference > variance or difference % 2 != variance % 2:
        # print(0.0)
        pass

    else:
        difference += variance
        difference //= 2
        c = factorial(variance) / (factorial(difference) * factorial(variance - difference))
        # print(c / (2 ** variance))
        pass


# 示例调用
if __name__ == "__main__":
    main(10)