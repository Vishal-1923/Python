# ************************************************* function caching **********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/92-Day-92-Function-Caching/.tutorial/Tutorial.md

# Function Caching: ek hi function ek hi value k lie kai baar run hota hai and we use memoization technique.

# we use it on those functions which are expensive (computationally).
# to implement it, we use functools module of python, which will maintain a LRU cache. and all the previous processed value will be stored in cache and next time when function calls for same value it does not do processing rather fetch value from cache itself.

'''
import functools

@functools.lru_cache(maxsize=None)
'''

# or


from functools import lru_cache as lc
import time

@lc(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*1

print(fx(10))
print("done for 10")
print(fx(100))
print("done for 100")
print(fx(1000))
print("done for 1000")
# as program ran for 1st time, it has stored values generated for these values in cache.
# now if i call it again it will not do any processing

print(fx(10))
print("done for 10")
print(fx(100))
print("done for 100")
print(fx(1000))
print("done for 1000")

# remember cache will be wiped out once program's execution is finished. It does not have lifetime memory

# also LRU cache takes memory so use it wisely