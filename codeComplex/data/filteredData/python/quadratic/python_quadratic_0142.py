from itertools import permutations

def main(n):
    # Generate four blocks of data, each with n rows of n columns
    # Values are deterministic based on indices and block index
    a = []
    for block_idx in range(4):
        block = []
        for i in range(n):
            row = [((i + j + block_idx) % 2) for j in range(n)]
            block.append(row)
        a.append(block)

    ans = 10 ** 10
    for perm in permutations(a, 4):
        cnt = 0
        total = 0
        for j in perm:
            if cnt < 2:
                cnt2 = 0
                for p in j:
                    for q in p:
                        if q != cnt2 % 2:
                            total += 1
                        cnt2 += 1

            else:
                cnt2 = 1
                for p in j:
                    for q in p:
                        if q != cnt2 % 2:
                            total += 1
                        cnt2 += 1
            cnt += 1

        ans = min(ans, total)

    # print(ans)
    pass
if __name__ == "__main__":
    main(5)