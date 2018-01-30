import string

'''
Return a tuple that contains a int and a list. The int indicates how many word the document has, and the list contains all the word it has.
file<file>: the document need to be handle. 
'''
def read_words(file):
    count = 0
    res_word_lst = []
    for lines in file:
        word_lst = lines.split()
        for word in word_lst:
            word = word.strip()
            word = word.translate(None,string.punctuation)
            word = word.lower()
            count += 1
            res_word_lst.append(word)
    return (count,res_word_lst)

def vocabulary(word_lst):
    d = dict()
    for word in word_lst:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

t = open('D:\\2-Study\skill_Python\Think Python\The Count of monte cristo.txt')
number_of_words,res_word_lst = read_words(t)
print res_word_lst
#d = vocabulary（res_word_lst）
print d