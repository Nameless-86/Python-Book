from Queue import Queue

if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    print(len(q))
    print(q.dequeue())
    # print(q.dequeue())
    print(q)
