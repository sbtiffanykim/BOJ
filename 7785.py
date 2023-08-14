# 7785_회사에 있는 사람
people = set()

n = int(input())
for _ in range(n):
    name, status = input().split()
    try:
        if status == 'enter':
            people.add(name)
        else:
            people.remove(name)
    except:
        continue

people = sorted(people, reverse=True)
print(*people, sep='\n')
