from doctest import run_docstring_examples

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('care', 'car')
    False
    """

    for i in word.lower():
        if   i not in available.lower():
            return False
    return True

run_docstring_examples (uses_only, globals(), verbose=True)