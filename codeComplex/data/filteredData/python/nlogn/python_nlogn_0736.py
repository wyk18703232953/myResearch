def main(n):
    # Deterministically generate array 'a' of length n
    # Example pattern: a[i] = i // 2  (creates duplicates, non-decreasing)
    a = [i // 2 for i in range(n)]
    a.sort()

    if not any(a):
        print('cslnb')
    elif n > 2 and a[0] == a[1] == 0:
        print('cslnb')
    else:
        seq_cnt = 0
        seq_sz = 1
        max_seq_sz = 1
        if n > 1:
            for i in range(n - 1):
                if a[i] == a[i + 1]:
                    seq_sz += 1
                elif a[i] + 1 == a[i + 1] and i + 2 < n and a[i + 1] == a[i + 2]:
                    max_seq_sz = 3
                    break
                else:
                    if seq_sz > max_seq_sz:
                        max_seq_sz = seq_sz
                    if seq_sz > 1:
                        seq_cnt += 1
                    seq_sz = 1

            if seq_sz > max_seq_sz:
                max_seq_sz = seq_sz
            if seq_sz > 1:
                seq_cnt += 1

        if max_seq_sz > 2 or seq_cnt > 1:
            print('cslnb')
        else:
            last = 0
            to_play = 0
            for i in range(n):
                to_play += a[i] - last
                last += 1

            if to_play % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')


if __name__ == "__main__":
    main(10)