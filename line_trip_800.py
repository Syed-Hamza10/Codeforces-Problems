def foo():
    n, x = map(int,input().split())

    arr = list(map(int,input().split()))
    capacity = arr[0]

    for i in range(1,len(arr)):
        if capacity < (arr[i] - arr[i-1]):
            capacity = arr[i] - arr[i-1]
    capacity = max(capacity,2*(x-arr[-1]))
    print(capacity)
        
test = int(input())
for _ in range(test):
    foo()

            