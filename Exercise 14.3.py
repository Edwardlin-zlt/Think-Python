from anagram_sets import *
import shelve

def store_anagrams(filename):
    '''
    analysis a file's words, and find out all the anagrams, then store it inside a shelf
    filename: A string of file's name
    '''
    data = shelve.open('anagrams_in_%s.dat' % filename.strip(), 'c')
    d = anagram_sets.all_anagrams(filename)
    for sig, words in d.iteritems():
        data[sig] = words
    data.close()

def read_anagrams(database, word):
     """
     Reads a anagram, looks up a word and returns a list of its anagrams.
     :param database: the name of database.
     :param word: A string of word that need to be looked up.
     :return: A list of its anagrams.
     """
     d = shelve.open(database)
     sig = signature(word)
     if sig in d:
         return d[sig]
     else:
         print 'There is no such a word'


if __name__ == '__main__':
    store_anagrams('words.txt')