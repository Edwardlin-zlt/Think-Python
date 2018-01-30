import random
'''
Return a dict whose key is the elements of lst, and value is the time that each element appear in the lst
lst: list
'''
def histogram(lst):
    d = dict()
    for element in lst:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d

def choose_from_hist(hist):
    key = hist.keys()
    amount_number = 0
    chosen_item = random.choice(key)
    for i in hist.values():
        amount_number += i
    probability = hist[chosen_item] / float(amount_number)
    return chosen_item,probability

t = ['a','a','a','b','c']

hist = histogram(t)
print choose_from_hist(hist)
