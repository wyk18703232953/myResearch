def main(n):
    if n < 2:
        # For n < 2, original logic (accessing arr[1]) is invalid.
        # Define smallest valid structure: replicate first element.
        n = 2

    # Deterministic generation of input array of length n
    # Example pattern: arr[i] = (i * 2 - (i // 3)) % 7
    arr = [((i * 2 - (i // 3)) % 7) for i in range(n)]

    pal = 1 if arr[1] > arr[0] else 3 if arr[0] == arr[1] else 5
    b = True
    arr_pal = [pal]
    for i in range(n - 2):
        if arr[i + 1] > arr[i]:
            if pal == 5:
                b = False
                break
            if arr[i + 2] < arr[i + 1]:
                pal = 5
                arr_pal.append(pal)

            else:
                pal += 1
                arr_pal.append(pal)
        elif arr[i + 1] < arr[i]:
            if pal == 1:
                b = False
                break
            if arr[i + 2] > arr[i + 1]:
                pal = 1
                arr_pal.append(pal)

            else:
                pal -= 1
                arr_pal.append(pal)

        else:
            if arr[i + 2] > arr[i + 1]:
                pal = 2 if pal == 1 else 1
                arr_pal.append(pal)
            elif arr[i + 2] < arr[i + 1]:
                pal = 4 if pal == 5 else 5
                arr_pal.append(pal)

            else:
                pal = 4 if pal < 4 else 3
                arr_pal.append(pal)
    if arr[-2] < arr[-1]:
        if pal == 5:
            b = False

        else:
            pal += 1
            arr_pal.append(pal)
    elif arr[-2] > arr[-1]:
        if pal == 1:
            b = False

        else:
            pal -= 1
            arr_pal.append(pal)

    else:
        pal = 3 if pal == 5 else 5
        arr_pal.append(pal)
    if b:
        # print(*arr_pal)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)