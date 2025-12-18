#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code

def main():
    n, q = map(int, input().split())
    for _ in range(q):
        node = int(input())
        s = input()

        for i in s:
            if i == 'L':
                if node % 2:
                    continue
                k = node & (-node)
                node -= k
                k //= 2
                node += k

            if i == 'R':
                if node % 2:
                    continue
                k = node & (-node)
                k //= 2
                node += k
            
            if i == 'U':
                if node == (n + 1) // 2:
                    continue
                k = node & (-node)
                node -= k
                k *= 2
                node |= k
        print(node)
    return

if __name__ == "__main__":
    main()