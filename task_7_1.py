from doctest import run_docstring_examples

def uses_none (word, forbiden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """

    for letter in word.lower():
        if letter in forbiden.lower():
            return False
    return True

run_docstring_examples(uses_none, globals(), verbose=True)
