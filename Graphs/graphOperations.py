class Graph:
    def __init__(self,graph = []):
        self.graph = graph
        self.nodes = []
        self.node_count = 0
    
    def add_node(self, node):
        if node in self.nodes:
            print("Node already present. Can't Add it")
        else:
            self.node_count += 1
            if type(self.graph) == list:
                print("Graph is represented as Adjacency Matirx")
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
    
    def DFS(self, node, visited):
        if node not in self.graph:
            print(f"Start Node {node} is not in the graph")
            return
        else:
            if node not in visited:
                visited.add(node)
                print(f"{node}", end="=>")
                for neighbor_node in self.graph[node]:
                    self.DFS(neighbor_node, visited)
                    
    def dfs_iterative(self, node):
        visited = set()
        if node not in self.graph:
            print(f"Start Node {node} is not in the graph")
            return
        else:
            stack = []
            stack.append(node)
            
            while stack:
                current = stack.pop()
                if current not in visited:
                    print(f"{current}", end="=>")
                    visited.add(current)
                    for item in self.graph[current]:
                        stack.append(item)

    def delete_node(self, node):
        self.node_count -= 1
        if type(self.graph) == list:
            if node not in self.nodes:
                print(f"Node {node} is not present in the Graph, Can't delete it.")
            else:      
                node_index = self.nodes.index(node)
                self.nodes.remove(node)
                self.graph.pop(node_index)
                for i in self.graph:
                    i.pop(node_index)
        else:
            if node not in self.graph:
                print(f"Node {node} is not present in the Graph, Can't delete it.")
            else:
                del self.graph[node]
                # for rows in self.graph:
                #     for items in rows:
                #         if node in items:
                #             items.remove(node)

    def add_graph_edge(self, node1, node2, cost=None):
            if type(self.graph) == list:
                if node1 not in self.nodes:
                    print(f"Node {node1} is not present in the graph. Can't add edge between {node1} and {node2}")
                elif node2 not in self.nodes:
                    print(f"Node {node2} is not present in the graph. Can't add edge between {node1} and {node2}")
                else:
                    if cost == None:
                        index1 = self.nodes.index(node1)
                        index2 = self.nodes.index(node2)
                        self.graph[index1][index2] = 1
                        self.graph[index2][index1] = 1
                    else:
                        index1 = self.nodes.index(node1)
                        index2 = self.nodes.index(node2)
                        self.graph[index1][index2] = cost
                        self.graph[index2][index1] = cost
            else:
                if node1 not in self.graph:
                    print(f"Node {node1} is not present in the graph. Can't add edge between {node1} and {node2}")
                    return
                elif node2 not in self.graph:
                    print(f"Node {node2} is not present in the graph. Can't add edge between {node1} and {node2}")
                    return
                else:
                    if cost == None:
                        self.graph.get(node1,[]).append(node2)
                        self.graph.get(node2,[]).append(node1)
                    else:
                        self.graph.get(node1,[]).append((node2, cost))
                        self.graph.get(node2,[]).append((node1, cost))
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

# graph_representation = []
# graph = Graph(graph_representation)
# graph.add_node("A")
# graph.add_node("B")
# #print(graph)
# print("After edge is created")
# graph.add_graph_edge("A","B", 10)
# print(graph)
# graph.add_graph_edge("A","C")
# print(graph)
# print("After node is deleted")
# graph.delete_node("A")
# print(graph)

# graph_representation = {}
# graph = Graph(graph_representation)
# graph.add_node("A")
# graph.add_node("B")
# graph.add_node("C")
# #print(graph)
# print("After edge is created")
# graph.add_graph_edge("A","B", 10)
# #print(graph)
# print("After edge is created")
# graph.add_graph_edge("A","C", 5)
# print(graph)
# print("After node is deleted")
# graph.delete_node("A")
# print(graph)

graph_representation = {}
graph = Graph(graph_representation)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_graph_edge("A","B")
graph.add_graph_edge("B","C")
graph.add_graph_edge("C","A")
graph.add_graph_edge("D","E")
graph.add_graph_edge("E","B")
print(graph)
visited = set()
graph.DFS('B', visited)
print("\nDFS in Iterative Way")
graph.dfs_iterative('A')