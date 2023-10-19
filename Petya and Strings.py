a = input()
b = input()
a = a.lower()
b = b.lower()
count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        if a[i]<b[i]:
            count-=1
            break
        else:
            count+=1
            break    
print(count)            


