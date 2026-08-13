total = 0 
count = 0

def has_e(word):
    for i in word:
        if i == 'E' or i == 'e':
            return True
    return False


for line in open ('words.txt'):
    word = line.strip()
    total += 1
    if has_e(word):
        count += 1

print(count)