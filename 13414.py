# 13414_수강신청

import sys

input = sys.stdin.readline
k, l = map(int, input().split())
students = dict()

# 학번-순서를 key-value로 입력받음
for i in range(l):
    # 중복되면 순서는 갱신
    students[input().rstrip()] = i

# 순서에 따라 정렬
students = sorted(students.items(), key=lambda x: x[1])

# 수강가능 인원보다 신청한 인원이 더 적으면 수강가능 인원 수를 신청한 인원 수로 바꿈
# k만큼 출력할 때 IndexError피하기 위함
if k > len(students):
    k = len(students)

for i in range(k):
    print(students[i][0])
