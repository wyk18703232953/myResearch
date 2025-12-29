tot, choc = [int(i) for i in input().split()]

bg = 1
end = tot

while bg <= end:
    mid = (bg + end) // 2  # 整数除法
    add = (mid * (mid + 1)) // 2  # 整数除法
    
    sub = tot - mid
    difference = add - sub
    
    if difference == choc:
        print(sub)
        break
    elif difference < choc:
        bg = mid + 1  # 需要更大的mid
    else:
        end = mid - 1  # 需要更小的mid
else:
    # 如果没找到精确解
    print("No exact solution found")
    # 或者输出最接近的值
    print(f"Closest: sub={tot - mid}, diff={difference}")