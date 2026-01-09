def main(n):
    # Generate deterministic s and t based on n
    # s length = n, digits cycle 0-9
    s = [str(i % 10) for i in range(n)]

    # t length = max(1, n-1), digits in reverse cycle 9-0
    m = max(1, n - 1)
    t = [str((9 - i) % 10) for i in range(m)]

    s_list = list(s)
    t_list = list(t)

    if len(s_list) < len(t_list):
        s_list.sort(reverse=True)
        # print(''.join(s_list))
        pass

    else:
        count = [0] * 10
        for elm in s_list:
            count[ord(elm) - ord('0')] += 1
        ans = []
        less = False
        for i in range(len(s_list)):
            for j in range(9, -1, -1):
                if not less:
                    if j <= ord(t_list[i]) - ord('0') and count[j] > 0:
                        if j < ord(t_list[i]) - ord('0'):
                            ans.append(chr(j + ord('0')))
                            count[j] -= 1
                            less = True
                            break

                        else:
                            curr_num = 0
                            for k in range(10):
                                if j == k:
                                    for _ in range(count[k] - 1):
                                        curr_num = curr_num * 10 + k

                                else:
                                    for _ in range(count[k]):
                                        curr_num = curr_num * 10 + k
                            rest_num = 0
                            for k in range(i + 1, len(s_list)):
                                if k < len(t_list):
                                    rest_num = rest_num * 10 + (ord(t_list[k]) - ord('0'))

                                else:
                                    # If t_list is shorter than s_list, remaining digits are treated as 0
                                    rest_num = rest_num * 10
                            if rest_num >= curr_num:
                                ans.append(chr(j + ord('0')))
                                count[j] -= 1
                                break

                            else:
                                continue

                else:
                    if count[j] > 0:
                        ans.append(chr(j + ord('0')))
                        count[j] -= 1
                        break
        # print(''.join(ans))
        pass
if __name__ == "__main__":
    main(10)