
def search_e (word):
    found_e = False
    for letter in word:
        if letter == 'E' or letter == 'e':
            found_e = True 

    if found_e :
        print('The word has an "e"')
    else:
        print('No letter "e"')
        
search_e ('sky')