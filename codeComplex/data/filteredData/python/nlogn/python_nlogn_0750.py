def main(n):
    # Deterministically generate input array of size n
    # Here we create a non-decreasing sequence with some controlled duplicates
    # to exercise the original logic.
    arr = [(i // 3) for i in range(n)]
    arr.sort()

    # Core logic from original program
    if n >= 2 and arr[0] == arr[1] == 0:
        # print("cslnb")
        pass

    else:
        flag = 0
        for i in range(n - 2):
            if arr[i] == arr[i + 1] == arr[i + 2]:
                flag = 1
                break
        if flag == 1:
            # print("cslnb")
            pass

        else:
            flag = 0
            ind = 0
            for i in range(n - 1):
                if arr[i] == arr[i + 1]:
                    ind = i
                    flag += 1
            if flag == 1 and ind > 0 and arr[ind - 1] == arr[ind] - 1:
                # print("cslnb")
                pass
            elif flag >= 2:
                # print("cslnb")
                pass

            else:
                safe = 0
                for i in range(n):
                    if arr[i] - i >= 0:
                        safe += arr[i] - i
                if safe % 2 == 0:
                    # print("cslnb")
                    pass

                else:
                    # print("sjfnb")
                    pass
if __name__ == "__main__":
    main(10)