# *************************************************** Generators *****************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/91-Day-91-Generators-in-Python/.tutorial/Tutorial.md

# Generators: to generate on the fly values

# special functions that allows u to create an iterable sequence of values.

# generator function returns generator object. but this obj does not store those values it generates them as and when needed.

def my_gen():
    for i in range(5):
        yield i #returns a generator and suspend execution, it will resume execution as soon as next value is requested by next() keyword

gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) this line will give error as range was from 0-4

# another way to use generator
for i in gen:
    print(i)


# it is definitely memory efficient!
# it will generate only when requested, they r lazy!

