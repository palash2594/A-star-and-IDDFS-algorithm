import math

class Heap:
    __slots__ = "items", "destination", "heuristic", "rows", "columns"

    def __init__(self, destination, heuristic, rows, columns):
        self.items = list()
        self.destination = destination
        self.heuristic = heuristic
        self.rows = rows
        self.columns = columns

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
        if self.heuristic == "manhattan":
            item = self.items[len(self.items) - 1]
            index = len(self.items) - 1
            while self.hasParent(index) and (self.destination - self.parent(index).value) > (self.destination - self.items[index].value):
                self.swap(index, self.getIndexOfParent(index))
                index = self.getIndexOfParent(index)

        elif self.heuristic == "euclidean":
            item = self.items[len(self.items) - 1]
            index = len(self.items) - 1
            while self.hasParent(index) and self.calcEuclideanDist(self.parent(index)) > self.calcEuclideanDist(self.items[index]):
                self.swap(index, self.getIndexOfParent(index))
                index = self.getIndexOfParent(index)

        elif self.heuristic == "random":
            item = self.items[len(self.items) - 1]
            index = len(self.items) - 1
            while self.hasParent(index) and self.calcRandomHeuristic(self.parent(index)) > self.calcRandomHeuristic(self.items[index]):
                self.swap(index, self.getIndexOfParent(index))
                index = self.getIndexOfParent(index)

        elif self.heuristic == "nocost":
            item = self.items[len(self.items) - 1]
            index = len(self.items) - 1
            while self.hasParent(index):
                self.swap(index, self.getIndexOfParent(index))
                index = self.getIndexOfParent(index)

    def heapifyDown(self):
        if self.heuristic == "manhattan":
            index = 0
            while self.hasLeftChild(index):
                smallerChildIndex = self.getIndexOfLeftChild(index)
                if self.hasRightChild(index) and (self.destination - self.rightChild(index).value) < (self.destination - self.leftChild(index).value):
                    smallerChildIndex = self.getIndexOfRightChild(index)

                if (self.destination - self.items[smallerChildIndex].value) < (self.destination - self.items[index].value):
                    self.swap(index, smallerChildIndex)
                    index = smallerChildIndex

                else:
                    break

        elif self.heuristic == "euclidean":
            index = 0
            while self.hasLeftChild(index):
                smallerChildIndex = self.getIndexOfLeftChild(index)
                if self.hasRightChild(index) and self.calcEuclideanDist(self.rightChild(index)) < self.calcEuclideanDist(self.leftChild(index)):
                    smallerChildIndex = self.getIndexOfRightChild(index)

                if self.calcEuclideanDist(self.items[smallerChildIndex]) < self.calcEuclideanDist(self.items[index]):
                    self.swap(index, smallerChildIndex)
                    index = smallerChildIndex

                else:
                    break

        elif self.heuristic == "random":
            index = 0
            while self.hasLeftChild(index):
                smallerChildIndex = self.getIndexOfLeftChild(index)
                if self.hasRightChild(index) and self.calcRandomHeuristic(self.rightChild(index)) < self.calcRandomHeuristic(self.leftChild(index)):
                    smallerChildIndex = self.getIndexOfRightChild(index)

                if self.calcRandomHeuristic(self.items[smallerChildIndex]) < self.calcRandomHeuristic(self.items[index]):
                    self.swap(index, smallerChildIndex)
                    index = smallerChildIndex

                else:
                    break

        elif self.heuristic == "nocost":
            index = 0
            while self.hasLeftChild(index):
                smallerChildIndex = self.getIndexOfLeftChild(index)
                if self.hasRightChild(index):
                    smallerChildIndex = self.getIndexOfRightChild(index)
                    self.swap(self.getIndexOfLeftChild(index), self.getIndexOfRightChild(index))

                self.swap(index, smallerChildIndex)
                index = smallerChildIndex

    def isempty(self):
        return len(self.items) == 0

    def calcEuclideanDist(self, node):
        x1 = node.value / self.rows
        y1 = (node.value - 1) % self.columns + 1

        return math.sqrt(math.pow((self.rows - x1), 2) + math.pow((self.columns - y1), 2))

    def calcRandomHeuristic(self, node):
        hashcode = hash(str(node.value))
        return hashcode / self.destination * 25


def main():
    size = 0
    items = list()
    heap = Heap()
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
