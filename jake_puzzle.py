words = {}
with open("c:\\temp\\datasets\\words.txt") as f:
    for line in f:
        words[line] = None

for x in words:
    if ('p' in x) and ('d' in x):
        if x.replace('p', 'g').replace('d', 'r') in words:
            print x, x.replace('p', 'g').replace('d', 'r')
