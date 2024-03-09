def foo():
    n, m = map(int, input().split())
    x = input()
    s = input()
    count = 0
    if s in x:
        return count
    else:
        for _ in s:
            if len(x) > len(s)//2 and count > len(s)//2:
                return -1
            count += 1
            x += x
            if s in x:
                return count
            else:
                continue
        return -1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(foo())