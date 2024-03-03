
def foo():
    n = int(input())
    s = input()
    if '...' in s:
        return 2
    else:
        count = 0
        for i in s:
            if i == '.':
                count += 1
    return count            

t = int(input())
for _ in range(t):
    print(foo())
