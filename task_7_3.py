from doctest import run_docstring_examples

def uses_all(word, required):
    """Check whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True

    >>> uses_all('apple', 'api')
    False
    """
    for i in required:
        if i not in word.lower():
            return False
    return True

run_docstring_examples(uses_all, globals(), verbose= True)
    