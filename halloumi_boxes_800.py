def foo(n,k,arr):    
    if k>=2 or is_sorted(arr):
        print("YES")
    else:
        print("NO")

def is_sorted(arr):
    if all(a<=b for a,b in zip(arr,arr[1:])):
        return True
    return False

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    foo(n,k,arr)