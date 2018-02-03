import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line = line.replace('-', ' ')            # what's the use of this statement
                                             # All the English word in a article are separated by spaces or hyphens
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace) # Punctuations could stick with a word, like `word,`, and they often at the the beginnings or ends of a word, so we use this statement to purify a word.
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

hist = process_file('The Count of monte cristo.txt')
print hist

print 'Total number of words:', total_words(hist)
print 'Number of different words:', different_words(hist)

t = most_common(hist)
print 'The most common words are:'
for freq, word in t[0:10]:
    print word, '\t', freq
