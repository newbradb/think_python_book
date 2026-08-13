total = 0 

for line in open ('words.txt'):
    word = line.strip()
    total += 1

print(total)