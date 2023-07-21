n = int(input())
users = []

for i in range(n):
    age, name = input().split()
    users.append((i, int(age), name))

users.sort(key=lambda x: (x[1], x[0]))
for i, age, name in users:
    print(age, name)
