import networkx as nx
import heapq
import matplotlib.pyplot as plt

def create_transport_graph():
    G = nx.Graph()
    
    for i in range(1, 11):
        G.add_node(i, label=f"Store:{i}")

    edges = [
        (1, 2, 4), (1, 3, 2), (2, 4, 5), (2, 5, 10), (3, 6, 3), (3, 7, 8),
        (4, 8, 6), (5, 9, 7), (6, 10, 1), (7, 8, 2), (8, 9, 9), (9, 10, 4)
    ]
    G.add_weighted_edges_from(edges)
         
    return G

def dijkstra(graph, start):
  
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def visualize_graph(G):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
                
def main():
    G = create_transport_graph()
    print(dijkstra(G, 1))
    visualize_graph(G)

if __name__ == "__main__":
    main()
