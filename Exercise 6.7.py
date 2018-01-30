def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif len(word) == 2:
        if word[0] == word[-1]:
            return True
    elif word[0] == word[-1]:
        word = middle(word)
        is_palindrome(word)
    else:
        return False
