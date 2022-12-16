from queues import Queue

# Testing 1
print("Testing 1")
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())
print("")

# Testing 2
print("Testing 2")
fifo = Queue("1st", "2nd", "3rd")
len(fifo)


for element in fifo:
    print(element)


len(fifo)