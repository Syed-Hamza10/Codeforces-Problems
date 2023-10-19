n = int(input())
count = 0
for i in range(n):
    X = input()
    if X == "++X" or X == "X++":
        count +=1
    elif X == "--X" or X == "X--":
        count-=1
print(count)    
