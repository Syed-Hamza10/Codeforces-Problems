def foo():
    a = input()
    lst = list(a)
    counter = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            counter += 1
            if counter == 7:
                return 'YES'
        else:
            counter = 1
    return 'NO'

print(foo())                

#00100110111111101