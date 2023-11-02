t = int(input())

for _ in range(t):
    stack = list()
    flag = True
    s = input()
    for c in s:
        # 열린 괄호일 때
        if c == '(':
            stack.append(c)
        # 닫힌 괄호일 때
        else:
            if stack:
                stack.pop()
            else:
                flag = False
                break

    if stack or (not flag):
        print('NO')
    else:
        print('YES')
