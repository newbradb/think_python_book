from doctest import run_docstring_examples

total = 0 
count = 0

def has_e(word):
    return 'e' in word.lower()

def uses_any(word, letters):
    """CHECKS if a word uses any of a list letters 
    >>> uses_any('banana','aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """

    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

run_docstring_examples(uses_any, globals(), verbose=True)


