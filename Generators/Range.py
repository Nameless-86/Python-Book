class Range():
    def __init__(self, stop: int) -> None:
        self.start = 0
        self.stop = stop

    def __iter__(self):
        curr = self.start
        while curr < self.stop:
            yield curr
            curr +=1



def range_example():
    for n in Range(1000):
        print(n)
        if n == 4:
            break

range_example()