# ******************************************* Async IO *********************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/96-Day-96-AsyncIO-in-Python/.tutorial/01-AsyncIOinPython.md

# used to do Asyncronous work via python

# it is neither multi-threading nor multi-processing but is just a way by which u can run yr code concurrently.

# it is a programming pattern that allows for high performance io operations in a concurrent and non-blocking manner.
# done using asyncio module and asynchronous functions.

# normal order of execution:
# function1
# function2
# function3
# when function1 finishes then function2 runs and so on 

# we can try to run 2 or more functions at same time via async programming.

import time
import asyncio

# async def function1():
#     # time.sleep(2)
#     await asyncio.sleep(1)
#     print("f1")

# async def function2():
#     # time.sleep(2)
#     await asyncio.sleep(1)
#     print("f2")

# async def function3():
#     # time.sleep(2)
#     await asyncio.sleep(4)
#     print("f3")

# function1()
# function2()
# function3()

# if we try to run this right now, it will give error i.e., these functions have never been awaited.
# async def main():
#     await function1()
#     await function2()
#     await function3()

# await means ki kisi bhi async function k finish hone ka intezar kr lo phir agla function chalao and so on...
# asyncio.run(main()) #isse abhi bhi ye ek ek kr k hi chalenge

# to run concurrently we can create an async task
# async def main():
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()

# asyncio.run(main())
# isse yeh hua ki pehle function2 chalega then jb bhi function1 ko time milega wo chal jaaega.
# so basically function1 is scheduled 

# but this does not provide better organization

async def function1():
    # time.sleep(2)
    await asyncio.sleep(1)
    print("f1")

async def function2():
    # time.sleep(2)
    await asyncio.sleep(1)
    print("f2")

async def function3():
    # time.sleep(2)
    await asyncio.sleep(4)
    print("f3")

async def main():
    l = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(l)

asyncio.run(main())
# isse ye teeno ek saath chalenge
# ye to ek basic example hai but hm isse complex kaam bhi krwa skte hai
