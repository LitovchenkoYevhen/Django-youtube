from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper




@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 ==0:
            l.append(i)
    return l

@timeit
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

# l1 = timeit(one)  # @timeit
# a = l1(10)

print(one(10))