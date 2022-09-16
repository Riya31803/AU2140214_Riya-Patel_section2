# Riya patel  AU2140214
# priority queues 

class PriorityQueueL:

    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._size = 0

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._size

    def enqueue(self, item, priority):

        node = _PriorityQEntryl(item, priority)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._size += 1

    def dequeue(self):

        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        node = self._qhead

        highpri = self._qhead.priority
        highnode = self._qhead


        while node != None:
            if node.priority < highpri:
                highpri = node.priority
                highnode = node
                prevhigh = prevnode
            prevnode = node
            node = node.next
        prevhigh.next=highnode.next
        self._size -=1
        return [highnode.item,highnode.priority]

    def printQ(self):
        node = self._qhead
        while node != None:
            print(node.item," ",node.priority)
            node=node.next

class _PriorityQEntryl:
  def __init__( self, item,priority ):
    self.item = item
    self.priority=priority
    self.next = None

Q = PriorityQueueL()
Q.enqueue( "USA", 2 )
Q.enqueue( "China", 5 )
Q.enqueue( "India", 0 )
Q.enqueue( "Russia", 1 )
Q.enqueue( "Australia", 1 )
Q.enqueue( "UK", 3 )
Q.printQ()
print("\nFirst dequeued element is ")
print(Q.dequeue())
print("\nsecond dequeued element is ")
print(Q.dequeue())
