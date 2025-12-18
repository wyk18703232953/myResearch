from collections import deque
with open("input.txt","r") as input_file: 
    with open("output.txt","a") as output_file:
        N,M = map(int,input_file.readline().split())
        K = int(input_file.readline())
        T = list(map(int,input_file.readline().split()))
        graph = [[0] * (M + 1) for _ in range(N + 1)]
        queue = deque()
        for i in range(0, 2 * K - 1, 2):
            graph[T[i]][T[i + 1]] = 1
            queue.append((T[i], T[i + 1]))
        x, y = 0, 0
        while queue:
            x, y = queue.popleft()
            x_moves = [x - 1, x + 1, x, x]
            y_moves = [y, y, y - 1, y + 1]
            for i in range(len(x_moves)):
                if 0 < x_moves[i] <= N and 0 < y_moves[i] <= M:
                    if graph[x_moves[i]][y_moves[i]] == 0:
                        x = x_moves[i]
                        y = y_moves[i]
                        graph[x_moves[i]][y_moves[i]] = 1
                        queue.append((x_moves[i], y_moves[i]))
        output_file.write(f"{x} {y}")