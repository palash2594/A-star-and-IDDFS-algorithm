class Vertex:
    __slots__ = "obstacle", "value", "edges"

    def __init__(self, value, obstacle=False):
        self.value = value
        self.obstacle = obstacle
        self.edges = dict()

    def __str__(self):
        return str(self.value) + " " + str(self.obstacle) + " " + str(self.edges)


class Graph:
    __slots__ = "vertices"

    def __init__(self):
        self.vertices = dict()

    def insertVertex(self, vertex):
        self.vertices[vertex.value] = vertex
        # self.edges[vertexID] = value

    def addEdges(self, vertex1, vertex2, value):
        if vertex1.value not in self.vertices:
            self.insertVertex(vertex1)
        if vertex2.value not in self.vertices:
            self.insertVertex(vertex2)

        self.vertices[vertex1.value].edges[vertex2.value] = value
        self.vertices[vertex2.value].edges[vertex1.value] = value

    def getVertex(self, value):
        if value in self.vertices.keys():
            return self.vertices[value]

        else:
            return None

    # def buildGraph(self):

    def __str__(self):
        return str(self.vertices)


def file_read(file):
    file_data = open(file, "r")
    maze = list()

    line_num = 0
    for line in file_data:
        line_data = line.strip().split(" ")
        maze.append(line_data)
        line_num += 1
    return maze


def prepare_graph(maze):
    graph = Graph()
    row = 0
    column = 0
    row_limit = len(maze)
    column_limit = len(maze[0])

    for i in range(row_limit):
        for j in range(column_limit):
            if maze[i][j] == "0":
                v = Vertex(j + i * column_limit + 1)
                graph.insertVertex(v)

    for i in range(row_limit):
        for j in range(column_limit):

            # look up
            if i >= 1 and maze[i - 1][j] == "0" and maze[i][j] == "0":
                v1 = graph.getVertex(j + i * column_limit + 1)
                v2 = graph.getVertex(j + (i - 1) * column_limit + 1)
                graph.addEdges(v1, v2, 0)

            # look down
            if i < row_limit - 1 and maze[i + 1][j] == "0" and maze[i][j] == "0":
                v1 = graph.getVertex(j + i * column_limit + 1)
                v2 = graph.getVertex(j + (i + 1) * column_limit + 1)
                graph.addEdges(v1, v2, 0)

            # look right
            if j < column_limit - 1 and maze[i][j + 1] == "0" and maze[i][j] == "0":
                v1 = graph.getVertex(j + i * column_limit + 1)
                v2 = graph.getVertex((j + 1) + (i) * column_limit + 1)
                graph.addEdges(v1, v2, 0)

            # look left
            if j > 0 and maze[i][j - 1] == "0" and maze[i][j] == "0":
                v1 = graph.getVertex(j + i * column_limit + 1)
                v2 = graph.getVertex((j - 1) + (i) * column_limit + 1)
                graph.addEdges(v1, v2, 0)

    return graph


def dfs(graph):
    # for key, value in graph.vertices.items():
    #     print(key, value)

    visited = list()
    to_explore = list()

    if (graph.getVertex(1)):
        to_explore.append(graph.getVertex(1))

        while to_explore:
            current = to_explore.pop()
            print("Current", current)
            if current.value == 200:
                print("Path exist")
                break
            visited.append(current.value)
            current_children = current.edges
            for key, value in current_children.items():
                if key not in visited:
                    to_explore.append(graph.getVertex(key))


    else:  # start point not present
        print("No path found")


def main():
    # v7 = Vertex(7)
    # v5 = Vertex(5)
    # v6 = Vertex(6)
    # v3 = Vertex(3)
    # v8 = Vertex(8)
    # v2 = Vertex(2)
    # v9 = Vertex(9)
    # v11 = Vertex(11)
    # v50 = Vertex(50)
    # v12 = Vertex(12)
    # v13 = Vertex(13)
    # v22 = Vertex(22)
    #
    # g = Graph()
    #
    # g.insertVertex(v7)
    # g.insertVertex(v5)
    # g.insertVertex(v6)
    # g.insertVertex(v3)
    # g.insertVertex(v8)
    # g.insertVertex(v2)
    # g.insertVertex(v9)
    # g.insertVertex(v11)
    # g.insertVertex(v50)
    # g.insertVertex(v12)
    # g.insertVertex(v13)
    # g.insertVertex(v22)
    #
    # g.addEdges(v7, v5, 20)
    # g.addEdges(v5, v6, 10)
    # g.addEdges(v5, v3, 30)
    # g.addEdges(v5, v8, 40)
    # g.addEdges(v9, v8, 40)
    # g.addEdges(v3, v2, 40)
    # g.addEdges(v2, v11, 40)
    # g.addEdges(v11, v9, 40)
    # g.addEdges(v2, v50, 40)
    # g.addEdges(v50, v12, 40)
    # g.addEdges(v12, v11, 40)
    # g.addEdges(v12, v13, 40)
    # g.addEdges(v50, v22, 40)
    #
    # print(g.getVertex(v7))
    # print(g.getVertex(v5))
    # print(g.getVertex(v6))
    # print(g.getVertex(v3))
    # print(g.getVertex(v8))
    # print(g.getVertex(v9))
    # print(g.getVertex(v2))
    # print(g.getVertex(v11))
    # print(g.getVertex(v50))
    # print(g.getVertex(v12))
    # print(g.getVertex(v13))
    # print(g.getVertex(v22))

    maze = file_read("test1")
    graph = prepare_graph(maze)

    # print(graph)

    dfs(graph)
    #
    # for key, value in graph.vertices.items():
    #     print(key, value)


if __name__ == '__main__':
    main()
