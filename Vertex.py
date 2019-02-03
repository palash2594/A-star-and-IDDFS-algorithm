class Vertex:
    __slots__ = "obstacle", "value", "edges"

    def __init__(self, value, obstacle=False):
        self.value = value
        self.obstacle = obstacle
        self.edges = dict()

    def __str__(self):
        return str(self.value) + " " + str(self.obstacle) + " " + str(self.edges)

vertex = Vertex(1, False)
vertex.insertNode(2, 5)
print(vertex)