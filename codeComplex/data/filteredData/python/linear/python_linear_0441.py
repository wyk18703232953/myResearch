ceil1 = lambda a, b: (a + b - 1) // b

def original_logic(n):
    sq = int(n ** 0.5)
    sq2, ans, cur = ceil1(n, sq), [], 0
    for _ in range(sq2 - 1):
        cur += sq
        ans.extend([x for x in range(cur, cur - sq, -1)])
    ans.extend([x for x in range(n, cur, -1)])
    return ans

def main(n):
    if n <= 0:
        return []
    result = original_logic(n)
    # print(' '.join(map(str, result)))
    pass
    return result

if __name__ == "__main__":
    main(10)