from queue import Queue
import queue
from queue import Queue

if __name__ == "__main__":
    queue = Queue()
    print(queue)

    queue.push(1)
    queue.push("Dennis")
    queue.push("Nice")
    queue.push(4)

    print(queue)

    queue.pop()

    print(queue)

    queue.peek()
    print(queue)
    print(len(queue))
