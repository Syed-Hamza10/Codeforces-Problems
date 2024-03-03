def foo():
    n = int(input())
    count = 1
    while count!= 11:
        if count % 2 == 1 and ((n+1)%3 == 0 or (n-1) % 3 == 0):
            return 'First'
        # elif count % 2 == 0 and
        count += 1
    return 'Second'     



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(foo())