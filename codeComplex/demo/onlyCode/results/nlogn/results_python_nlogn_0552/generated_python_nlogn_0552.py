def main(n):
    board = list(range(1, n + 1))
    board.insert(0, 0)
    hashed = [0] * (n + 1)
    for i in range(n + 1):
        hashed[board[i]] = i
    answer = ['C'] * (n + 1)
    for i in range(n, 0, -1):
        flag = 0
        k = hashed[i] - board[hashed[i]]
        while k > 0:
            if answer[k] == 'B':
                flag = 1
                break
            k -= board[hashed[i]]
        k = hashed[i] + board[hashed[i]]
        while k <= n and k != 0:
            if answer[k] == 'B':
                flag = 1
                break
            k += board[hashed[i]]
        if flag == 1:
            answer[hashed[i]] = 'A'
        else:
            answer[hashed[i]] = 'B'
    answer.pop(0)
    result = ''.join(answer)
    print(result)
    return result

if __name__ == "__main__":
    main(10)