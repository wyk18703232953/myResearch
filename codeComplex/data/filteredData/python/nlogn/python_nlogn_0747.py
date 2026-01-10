def main(n):
    # Generate deterministic input of size n
    a = [i // 2 for i in range(n)]
    a.sort()
    a_count = len(a)

    b = list(filter(lambda i: i > 0, a))
    b_count = len(b)

    def resh():
        idx = 1
        while idx < a_count:
            if a[idx] == a[idx - 1] and (a[idx] - 1) in a:
                return 'cslnb'
            idx += 1

        b_sum = sum(b)
        v_sum = sum(range(1, b_count if a_count == b_count else b_count + 1))
        t = max(b_sum - v_sum, 0)
        return 'cslnb' if t % 2 == 0 else 'sjfnb'

    if b_count == 0 or b_count - len(set(b)) > 1 or a_count - b_count > 1:
        result = 'cslnb'
    else:
        result = resh()

    return result


if __name__ == "__main__":
    # Example deterministic call
    print(main(10))