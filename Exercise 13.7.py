import string

def process_file(file):
    hist = dict()
    for line in file:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        hist[word] = hist.get(word, 0) + 1

f = open('D:\\2-Study\skill_Python\Think Python\The Count of monte cristo.txt')
hist = process_file(f)

keys = hist.keys()

