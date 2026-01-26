n = int(input())

a = sorted(map(int, input().split()))

if not any(a):
    print('cslnb')
elif n > 2 and a[0] == a[1] == 0:
    print('cslnb')
else:
    seq_cnt = 0
    seq_sz = 1
    max_seq_sz = 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            seq_sz += 1
        elif a[i] + 1 == a[i+1] and i + 2 < n and a[i+1] == a[i+2]:
            max_seq_sz = 3
            break
        else:
            max_seq_sz = max(seq_sz, max_seq_sz)
            seq_cnt += seq_sz > 1
            seq_sz = 1

    max_seq_sz = max(seq_sz, max_seq_sz)
    seq_cnt += seq_sz > 1

    if max_seq_sz > 2 or seq_cnt > 1:
        print('cslnb')
    else:
        last = to_play = 0
        for i in range(n):
            to_play += a[i] - last
            last += 1

        if to_play % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
