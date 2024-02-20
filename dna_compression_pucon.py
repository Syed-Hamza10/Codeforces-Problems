


def foo(s):
    current_num = 0
    stack = []
    current_str = ''
    for char in s:
        if char.isdigit():
            current_num = current_num*10 + int(char)
        elif char == '[':
            stack.append((current_num,current_str))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_num, prev_str = stack.pop() 
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char
    return current_str    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(foo(s))                   