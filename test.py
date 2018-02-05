def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    t.sort()
    print "1:",t
    t = ''.join(t)
    print '2:',t
    return t

signature('edward')