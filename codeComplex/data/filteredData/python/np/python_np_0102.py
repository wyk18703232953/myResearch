from math import factorial

def compute_probability(send, receive):
    cntP = send.count("+")
    cntN = send.count("-")

    cnt1 = receive.count("+")
    cnt2 = receive.count("-")

    mark = receive.count("?")
    total = pow(2, mark)

    if cntP < cnt1 or cntN < cnt2:
        valid = 0
    else:
        valid = factorial(mark) / factorial(mark - cntP + cnt1) / factorial(cntP - cnt1)

    return valid / total if total != 0 else 0.0

def main(n):
    if n <= 0:
        send = ""
        receive = ""
        result = compute_probability(send, receive)
        print(f"{result:0.12f}")
        return

    # Deterministically construct send and receive based on n
    # send: first n positions are '+' if i % 2 == 0 else '-', rest up to 2n are '-'
    send_list = []
    for i in range(n):
        send_list.append("+" if i % 2 == 0 else "-")
    for i in range(n, 2 * n):
        send_list.append("-")
    send = "".join(send_list)

    # receive: length 2n, pattern depends on i % 3
    # 0 -> '+', 1 -> '-', 2 -> '?'
    receive_list = []
    for i in range(2 * n):
        r = i % 3
        if r == 0:
            receive_list.append("+")
        elif r == 1:
            receive_list.append("-")
        else:
            receive_list.append("?")
    receive = "".join(receive_list)

    result = compute_probability(send, receive)
    print(f"{result:0.12f}")

if __name__ == "__main__":
    main(5)