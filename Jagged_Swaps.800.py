def foo():
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(1,n):
        if arr[0] > arr[i]:
            return 'NO'

    for i in range(1,n-1):
        if arr[0] > arr[1]:
            return 'No'
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i+1]

    return "YES"   





if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(foo())