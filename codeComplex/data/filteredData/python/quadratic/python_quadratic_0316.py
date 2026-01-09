def main(n):
    # Map n to original n and k, and generate deterministic arr
    original_n = n
    k = max(1, original_n // 2)
    arr = [i % 1000 for i in range(1, original_n + 1)]

    avg = 0
    for i in range(original_n):
        cnt = 0
        sum_val = 0
        for j in range(i, original_n):
            sum_val += arr[j]
            cnt += 1
            if cnt >= k:
                current_avg = sum_val / cnt
                if current_avg > avg:
                    avg = current_avg
    # print(avg)
    pass
if __name__ == "__main__":
    main(1000)