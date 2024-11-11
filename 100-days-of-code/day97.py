# ****************************************** Multi Threading ***************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/97-Day-97-MultiThreading-in-Python/.tutorial/01-multithreading.md

# When u want to download resources parallely from internet.
# done via threading module

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return sec

# time1 = time.perf_counter()
# func(5)
# func(3)
# func(1)
# time2 = time.perf_counter()
# print(time2 - time1)


# time1 = time.perf_counter()
# # we can make it run concurrently via threading.
# t1 = threading.Thread(target=func, args=[5])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[1])
# # have to manually start it
# t1.start()
# t2.start()
# t3.start()
# time2 = time.perf_counter()
# print(time2 - time1)
# ye sirf ye kr rha hai ki start kia aur side main rkh dia hm iske khtm hone ka wait hi ni kia
# inke khtm hone ka wait krne k lie we'll use join

# time1 = time.perf_counter()
# # we can make it run concurrently via threading.
# t1 = threading.Thread(target=func, args=[5])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[1])
# # have to manually start it
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(time2 - time1)

# more usefull when u want to download something as then the task is IO bound and not CPU bound

# we have something named as concurrent.futures
# it has threadpoolexecutor to whom we can submit functions and take its result.
def main():
    time1 = time.perf_counter()
    # we can make it run concurrently via threading.
    t1 = threading.Thread(target=func, args=[5])
    t2 = threading.Thread(target=func, args=[3])
    t3 = threading.Thread(target=func, args=[1])
    # have to manually start it
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:#used when u want to schedule tasks in bulk
        future = executor.submit(func, 5)
        print(future.result())
        future = executor.submit(func, 3)
        print(future.result())
        future = executor.submit(func, 1)
        print(future.result())
# poolingDemo()

# there is another syntax to use it -> via map

def poolingDemoWithMap():
    with ThreadPoolExecutor() as executor:
        l = [1, 2, 3, 4, 5]
        results = executor.map(func, l)
        for result in results:
            print(result)
poolingDemoWithMap()

# map syntax tb beneficial hai jb ek list main multiple links d rkhe ho and aapko un sbko download marna ho
