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
    for letter in word:
        if letter not in required.lower():
            return False
        
        elif letter in avaliable.lower():
            return True
    return True

run_docstring_examples (check_word, globals(), verbose=True)