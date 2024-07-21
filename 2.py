import networkx as nx
from collections import deque

def create_transport_graph():
    G = nx.Graph()
    
    for i in range(1, 11):
        G.add_node(i, label=f"Store:{i}")

    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
        (4, 8), (5, 9), (6, 10), (7, 8), (8, 9), (9, 10)
    ]
    G.add_edges_from(edges)

    return G

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
            
def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

        
def main():
    G = create_transport_graph()
 
    dfs_recursive(G, 1)
    print("")
    bfs_recursive(G, deque([1]))

if __name__ == "__main__":
    main()
