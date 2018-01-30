words = open('words.txt')
eng2sp = dict()
for word in words:
    eng2sp['%s' % word] = ''

key1 = eng2sp.keys()
for i in key1:
    print i
if 'ooters' in key1:
    print True
else:
    print False