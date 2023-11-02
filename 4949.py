while True:
    s = input()
    # 온점 하나 나오면 종료
    if s == '.':
        break

    flag = False
    parenthesis = {']': '[', ')': '('}

    stack = []
    for c in s:
        # 열리는 괄호면 stack에 추가
        if c in parenthesis.values():
            stack.append(c)
        # 닫히는 괄호일 때
        elif c in parenthesis:
            # stack에 값이 있고, 가장 최근에 등장한 열린 괄호가 지금 닫히는 괄호와 짝을 이루면
            if stack and stack[-1] == parenthesis[c]:
                # stack에서 열린 괄호 제거
                stack.pop()
            # stack에 값이 있는데 짝이 맞지 않거나, stack이 비어있으면
            else:
                # 균형이 맞지 않음
                flag = True

    # stack에 값 남아있거나, 앞에서 설정한 flag가 true라면 균형이 맞지 않음
    if stack or flag == True:
        print('no')
    else:
        print('yes')
