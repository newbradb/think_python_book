from doctest import run_docstring_examples

def check_word(word, avaliable, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) <= 3:
        return False

    for letter in required.lower():
         if letter not in word.lower():
            return False

    for letter in word.lower():
        if letter not in avaliable.lower():
            return False

    return True

def word_score(word, avaliable): 
    """Compute the score for acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15    
    """
    score = 0 

    for letter in word.lower():
            if letter not in avaliable.lower():
                raise ValueError ('No letters avaliable in the word')

    if len (word) == 4:
        if avaliable.lower in word.lower():
            score = 1

    if len (word) > 4:
         if avaliable.lower in word.lower():
             score += 1

    for i in word:
        if i not in word.lower():
            return False
    score += 7


run_docstring_examples (word_score, globals(), verbose=True)