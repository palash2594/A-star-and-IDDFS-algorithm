class Minheap:
    __slots__ = "items"

    def __init__(self):
        self.items = list()

    def getIndexOfLeftChild(self, parentIndex):
        return 2 * parentIndex + 1;

    def getIndexOfRightChild(self, parentIndex):
        return 2 * parentIndex + 2;

    def getIndexOfParent(self, childIndex):
        return (childIndex - 1) // 2;

    def hasLeftChild(self, index):
        return self.getIndexOfLeftChild(index) < len(self.items)

    def hasRightChild(self, index):
        return self.getIndexOfRightChild(index) < len(self.items)

    def hasParent(self, index):
        return self.getIndexOfParent(index) >= 0

    def leftChild(self, index):
        return self.items[self.getIndexOfLeftChild(index)]

    def rightChild(self, index):
        return self.items[self.getIndexOfRightChild(index)]

    def parent(self, index):
        return self.items[self.getIndexOfParent(index)]

    def swap(self, index1, index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def peek(self):
        return self.items[0]

    def poll(self):
        if not self.items:
            return None
        item = self.items[0]
        self.items[0] = self.items[len(self.items) - 1]
        self.heapifyDown()
        del self.items[-1]
        return item

    def addElement(self, item):
        self.items.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        item = self.items[len(self.items) - 1]
        index = len(self.items) - 1
        while self.hasParent(index) and self.parent(index).value > self.items[index].value:
            self.swap(index, self.getIndexOfParent(index))
            index = self.getIndexOfParent(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getIndexOfLeftChild(index)
            if self.hasRightChild(index) and self.rightChild(index).value < self.leftChild(index).value:
                smallerChildIndex = self.getIndexOfRightChild(index)

            if self.items[smallerChildIndex].value < self.items[index].value:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex

            else:
                break

    def isempty(self):
        return len(self.items) == 0

def main():
    size = 0
    items = list()
    heap = Minheap()
    heap.addElement(2)
    heap.addElement(3)
    heap.addElement(10)
    heap.addElement(20)
    heap.addElement(6)

    print(heap.poll())
    print(heap.poll())
    print(heap.poll())
    print(heap.poll())
    print(heap.poll())



if __name__ == '__main__':
    main()
