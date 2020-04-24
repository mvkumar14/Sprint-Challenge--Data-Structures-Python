import time
from lru_cache import LRUCache

print("\n\nMVP:")
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [] # Return the list of duplicates in this data structure
# duplicates1 = []  

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates1.append(name_1)

# THE RUNTIME FOR THE ABOVE CODE IS: O(n*m) [aka O(n^2)]
# where n is the length of one list and m is the length of the other
# in this case it is O(n^2) cause the lists are the same length 
# for every element in one list you loop through the other list once
# and you do a comparison.


# started doing it the following way:
    # I'm going to initalize an lru cache with a capacity of 20,000
    # when things are accessed again they move to the front of the cache
    # for every item in the cache loop through one list, and when 
    # you don't find a match that is when you know you have hit the part 
    # of the list without duplicates.
# but realized:
    # or you can just try to get the value... if it exists it will return
    # if not it won't. The runtime is based on dictionary access. 
    # this might be how set is implimented in the backend?

# the lesson here is that you learn as you code, so start moving, and 
# iterate on the first pass

my_limit = 10000
my_cache = LRUCache(limit=my_limit)
# this first part runs in O(n) time
for name_1 in names_1:
    my_cache.set(name_1,name_1)
# this second part runs in ?? 
# O(1) per dictionary access but 
# there are n dictionary accesses 
# I'm not sure how fast this part is.
for name_1 in names_2:
    value = my_cache.get(name_1)
    if value is not None:
        duplicates.append(value)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")

# this is how I checked that I got the same answer
# print(f"duplicates1:\n\n {', '.join(duplicates1)}\n\n")
# print(set(duplicates)-set(duplicates1))
print (f"runtime: {end_time - start_time} seconds\n\n")

# ---------- Stretch Goal 1-----------
# didn't want to do this. but maybe there is a better way.
# print('STRETCH 1:')
#     # sort each of the lists, and then
#     # do a binary search on the lists.

#     # the sorting time would be proportional to n
#     # the binary search would be log(n)
# start_time = time.time()
# duplicates = []
# if
# end_time = time.time()

# print(f"{len(union)} duplicates:\n\n{', '.join(union)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
# ---------- Stretch Goal 2-----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

print('STRETCH 2:')
start_time = time.time()

a = set(names_1) 
b = set(names_2)
union = a & b

end_time = time.time()

print(f"{len(union)} duplicates:\n\n{', '.join(union)}\n\n")
print (f"runtime: {end_time - start_time} seconds")