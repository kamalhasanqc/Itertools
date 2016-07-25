"""
This script gives a demo about some itertools, the core purpose of writing this script is to explore
Itertools and explore as much as I can.
"""
from itertools import *
from operator import itemgetter
"""
Chain functions returns elements from it's first iterable until it's exhausted
then from the second one
"""
print "Chain demo"
for x in chain([1, 2, 3], ['a', 'b', 'c']):
    print x
print '_'*10

# Cycle iterate the iterables appends them in array returns the array and start again
print "Cycle demo"
for x in cycle([1, 2, 3, 4, 5]):
    if x < 5:
        print x
    else:
        break
print '_'*10

# Returns an object repeatedly or n times
print "Repeat demo"
for x in repeat('kamal', 2):
    print x
print '_'*10

# Compress itertool returns only those elements who has 1 against key element
print "Compress itertool demo"
for x in compress([1, 2, 3], [0, 1, 1]):
    print x
print '_'*10

# Dropwhile itertool drops element of iterable until predicate is true after that it returns all elements
print "Dropwhile demo"
for x in dropwhile(lambda i: i < 5, [1, 2, 3, 6, 4, 2, 1]):
    print x
print '_'*10

# Izip itertool makes tuples of passed iterables with same indexing
print "izip demo"
for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
print '_'*10

# Islice method slices the iterable according to te arguments passed
#  It takes list,start,step,stop as parameters
print "islice demo"
print 'Stops at 5:'
for i in islice(count(), 5):
    print i

print 'Start at 5, Stop at 10:'
for i in islice(count(), 5, 10):
    print i

print 'By tens to 100:'
for i in islice(count(), 0, 100, 10):
    print i
print '_'*10

# Tee itertool returns by default two iterables from a given single iterable
print "Tee demo"
i1, i2 = tee(islice(count(), 5), 2)
for i in i1:
    print "i1: ", i
for i in i2:
    print "i2: ", i
print '_'*10

# Imap function runs the function for every iterable and returns tuples
print "imap demo"
for i in imap(lambda y, z: (2*y,  z), xrange(5), xrange(5, 11)):
    print i
print '_'*10

# Takewhile itertool saves element of iterable until predicate is true after that it stops it's execution
print "Takewhile demo"
for x in takewhile(lambda k: k < 5, [1, 2, 3, 6, 4, 2, 1]):
    print x
print '_'*10

# Ifilter filters the iterable until iterables are exhausted
print "Ifilter demo"
for x in ifilter(lambda k: k < 1, [0, -1, 1, -2, -3, 2, -4]):
    print x
print '_'*10

# Groupby itertool returns consecutive keys and groups from the iterable
print "Groupby demo"
temp_dict = dict(a=1, b=2, c=1, d=2)
sorted_dict = sorted(temp_dict.items(), key=itemgetter(1))
for x, k in groupby(sorted_dict, key=itemgetter(1)):
    print x, map(itemgetter(0), k)
print '_'*10
