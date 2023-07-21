s = input()
words = []

for i in range(len(s)):
    words.append(s[i:])

words.sort()
print(*words, sep='\n')
