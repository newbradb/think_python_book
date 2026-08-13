total = 0 
count = 0

def has_e(word):
    return 'e' in word.lower()
            
for line in open ('words.txt'):
    word = line.strip()
    total += 1
    if has_e(word):
        count += 1

print(count)