def foo(a,t):
    maxa = max(a)
    mini = min(a)
    return maxa - mini

t = int(input()) 
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split())) 
    print(foo(a, t))  
