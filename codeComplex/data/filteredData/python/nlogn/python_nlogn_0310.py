import random

#---------------- Merge Sort Inversion Counter ----------------#

def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)

def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for idx in range(left, right + 1):
        arr[idx] = temp_arr[idx]

    return inv_count

#------------------------- Main Logic -------------------------#

def main(n):
    # 3. 根据 n 生成测试数据：生成一个 1..n 的随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 原逻辑
    r = mergeSort(a, n)
    if r % 2 == (3 * n) % 2:
        print("Petr")
    else:
        print("Um_nik")

# 示例调用（评测时可由外部调用 main(n)）
if __name__ == "__main__":
    main(10)