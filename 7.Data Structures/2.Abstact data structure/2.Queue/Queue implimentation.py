class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,ele):
        if not self.queue:
            return print('Empty queue')
        self.queue.insert(0,ele)
        return
    
    def dequeue(self):
        return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]

    def isEmpty(self):
        return not self.queue
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=" ")
        print()
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.show()
q.dequeue()
q.show()