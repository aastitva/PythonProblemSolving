class Graph:
    def __init__(self,graph = []):
        self.graph = graph
        self.nodes = []
        self.node_count = 0
    
    def add_node(self, node):
        if node in self.nodes:
            print("Node already present. Can't Add it")
        else:
            if type(self.graph) == list:
                print("Graph is represented as Adjacency Matirx")
                self.node_count += 1
                self.nodes.append(node)
                
                if not self.graph:
                    self.graph = [[0]]
                    return
                for row in self.graph:
                    row.append(0)
                new_row = [0] * len(self.graph[0])
                self.graph.append(new_row)
            else:
                print("Graph is represented as Adjacency List")
                if node in self.graph:
                    print(f"Node {node} is already present")
                else:
                    self.graph[node] = []
    
    def add_graph_edge(self, node1, node2):
            if type(self.graph) == list:
                if node1 not in self.nodes:
                    print(f"Node {node1} is not present in the graph. Can't add edge between {node1} and {node2}")
                elif node2 not in self.nodes:
                    print(f"Node {node2} is not present in the graph. Can't add edge between {node1} and {node2}")
                else:
                    index1 = self.nodes.index(node1)
                    index2 = self.nodes.index(node2)
                    self.graph[index1][index2] = 1
                    self.graph[index2][index1] = 1
            else:
                if node1 not in self.graph:
                    print(f"Node {node1} is not present in the graph. Can't add edge between {node1} and {node2}")
                    return
                elif node2 not in self.graph:
                    print(f"Node {node2} is not present in the graph. Can't add edge between {node1} and {node2}")
                    return
                else:
                    self.graph.get(node1,[]).append(node2)
                    self.graph.get(node2,[]).append(node1)
            print(self.graph)


    def __str__(self):
        if type(self.graph) == list:
            result = []
            for row in self.graph:
                row_str = " ".join([str(x) for x in row])  # Using list comprehension instead of map
                result.append(row_str)
            return "\n".join(result)
        else:
            result = ""
            for node, neighbour in self.graph.items():
                result += str(f"{node} : {neighbour} \n")
            return "".join(result)

graph_representation = []
graph = Graph(graph_representation)
graph.add_node("A")
graph.add_node("B")
print(graph)
print("After edge is created")
graph.add_graph_edge("A","B")
print(graph)
graph.add_graph_edge("A","C")
print(graph)

graph_representation = {}
graph = Graph(graph_representation)
graph.add_node("A")
graph.add_node("B")
print(graph)
print("After edge is created")
graph.add_graph_edge("A","B")
print(graph)
graph.add_graph_edge("A","C")
print(graph)