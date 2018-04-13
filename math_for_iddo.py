

import random

while True:
    a = random.randint(1,70)
    b = raw_input(str(a) + "\n")
    if int(b) == a+1:
        print " _ \n/ \\\n\\_/"
    else:
        print " _ \n/ \\"

'''
while True:
    a = random.randint(2, 10)
    b = random.randint(1, a-1)
    c = raw_input("{} - {} = ?\n".format(a,b))
    if int(c) == a - b:
        print "/\\/\\/\\\n\n"
    else:
        print "/\n\n"
'''