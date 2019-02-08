import time
from Heap import Heap


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


def iddfs1(graph, depth, row, column):
    # for key, value in graph.vertices.items():
    #     print(key, value)

    current_depth = 0
    path_flag = False
    visited = list()
    to_explore = dict()

    if (graph.getVertex(1)):
        to_explore[graph.getVertex(1)] = 1

        while to_explore:
            for key, value in to_explore.items():
                current = key
                # print(type(key))
                current_depth = value
                to_explore.pop(key)
                break
            # print("Current", current)
            # print(current.value, "--> ", end="")
            if current.value == row * column:
                path_flag = True
                print("Path exist")
                return True
                break
            visited.append(current.value)
            current_children = current.edges
            for key, value in current_children.items():
                if key not in visited and current_depth <= depth:
                    to_explore[graph.getVertex(key)] = current_depth + 1

    if depth % 10 == 0:
        print(depth)


    else:  # start point not present
        # print("No path found")
        pass

    if path_flag is False:
        # print("No Path Found")
        return False

    print("depth", depth)
    print("_________________________*************************************_________________________")


def iddfs(graph, depth, row, column):
    # for key, value in graph.vertices.items():
    #     print(key, value)

    current_depth = 0
    path_flag = False
    visited = list()
    to_explore = list()

    if (graph.getVertex(1)):
        to_explore.append(graph.getVertex(1))

        while to_explore and current_depth <= depth:
            current = to_explore.pop()
            # print("Current", current)
            # print(current.value, "--> ", end="")
            if current.value == row * column:
                path_flag = True
                print("Path exist")
                return True
                break
            visited.append(current.value)
            current_children = current.edges
            for key, value in current_children.items():
                if key not in visited:
                    to_explore.append(graph.getVertex(key))

            current_depth += 1


    else:  # start point not present
        # print("No path found")
        pass

    if path_flag is False:
        # print("No Path Found")
        return False

    print("depth", depth)
    print("_________________________*************************************_________________________")


def a_star(graph, heuristic, rows, columns):
    visited = list()
    heap = Heap(rows * columns, heuristic, rows, columns)
    pathFound = False
    depth = 0

    if (graph.getVertex(1)):
        # to_explore.append(graph.getVertex(1))
        heap.addElement(graph.getVertex(1))

        while not heap.isempty():
            depth += 1
            if depth % 500 == 0:
                print(depth)
            # current = to_explore.pop()
            current = heap.poll()
            # print(current.value, "--> ", end=" ")
            if current.value == rows * columns:
                pathFound = True
                break
            # print("current", current)
            current_children = current.edges

            for key, value in current_children.items():
                if key not in visited:
                    visited.append(key)
                    heap.addElement(graph.getVertex(key))

    if pathFound == True:
        print("Nodes explored", depth)
    else:
        print("no path found")

def main():
    print("hello")
    # v7 = Vertex(7)
    # v5 = Vertex(5)

    # g = Graph()
    #
    # g.insertVertex(v7)
    # g.insertVertex(v5)

    # g.addEdges(v7, v5, 20)

    # print(g.getVertex(v7))

    maze = file_read("test1")
    graph = prepare_graph(maze)
    rows = len(maze)
    columns = len(maze[0])

    # print(graph)

    start_time = time.time()

    # ************* IDDFS *************** #

    # for i in range(rows * columns):
    #     path_found = iddfs1(graph, i, rows, columns)
    #     if path_found is True:
    #         print("Path found at depth: ", i + 1)
    #         break
    #
    # if path_found == False:
    #     print("No path found.")

    # ************* IDDFS *************** #

    print("Time taken in IDDFS -> %s seconds" % (time.time() - start_time))

    print(len(maze), len(maze[0]))

    # ************* A-Star Manhattan*************** #

    start_time = time.time()
    print("A-Star (Manhattan) started")

    a_star(graph, "manhattan", rows, columns)

    print("Time taken in A-Star Manhattan -> %s seconds" % (time.time() - start_time))

    # ************* A-Star Manhattan *************** #

    # ************* A-Star Euclidean *************** #

    start_time = time.time()
    print()
    print("A-Star(Euclidean) started")

    a_star(graph, "euclidean", rows, columns)

    print("Time taken in A-Star Euclidean -> %s seconds" % (time.time() - start_time))

    # ************* A-Star Euclidean *************** #

    # ************* A-Star Random Heuristic *************** #

    start_time = time.time()
    print()
    print("A-Star(Random Heuristic) started")

    a_star(graph, "random", rows, columns)

    print("Time taken in A-Star Random Heuristic -> %s seconds" % (time.time() - start_time))

    # ************* A-Star Random Heuristic *************** #

    # ************* A-Star No Cost Heuristic *************** #

    start_time = time.time()
    print()
    print("A-Star(No Cost Heuristic) started")

    a_star(graph, "nocost", rows, columns)

    print("Time taken in A-Star No Cost Heuristic -> %s seconds" % (time.time() - start_time))

    # ************* A-Star No Cost Heuristic *************** #

    #
    # for key, value in graph.vertices.items():
    #     print(key, value)


if __name__ == '__main__':
    main()
