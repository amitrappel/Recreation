__author__ = 'Amit Rappel'


n = 17
min_take = 1
max_take = 3

heap = n*[0]
print ' '.join(heap)
while len(heap) > 1:
    print "Heap:", ' '.join(heap)
    turn = raw_input("How many coins do you want to take?\n")
    while int(turn) not in range(min_take, max_take+1):
        turn = raw_input("You must take between {} and {}. Please choose again.".format(min_take, max_take))
    heap =