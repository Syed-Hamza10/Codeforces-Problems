def foo(n, arr):

    hash = {}

    for i in range(n):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1
    
    if len(hash) >= 3:
        print('NO')
    elif len(hash) == 1:
        print('YES')
    else:
        temp = list(hash.values())
        res = abs(temp[0] - temp[1])
        if res <= 1:
            print("YES")
        else:
            print("NO")


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    foo(n , arr)