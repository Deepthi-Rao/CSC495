from collections import deque
import threading

#This is the Queue class
class Queue:

    #this initializes the queue object
    def __init__(self):
        self.queue = deque([])

    #this enqueues an element to the end of the list
    def enqueue(self, element):
        self.queue.append(element)


    #this dequeues an element from the front of the list
    def dequeue(self):
        return self.queue.popleft()

    #this returns true if the queue is not empty
    def notEmpty(self):
        return len(self.queue) > 0

    def peek(self):
        return self.queue[0]

