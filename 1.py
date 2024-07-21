import networkx as nx
import matplotlib.pyplot as plt

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

def visualize_graph(G):
    labels = nx.get_node_attributes(G, 'label')
    
    num_nodes = G.number_of_nodes()  
    num_edges = G.number_of_edges()  
    
    options = {
        "node_color": "lightblue",
        "edge_color": "green",
        "node_size": 500,
        "width": 3,
        "labels": labels,
        "with_labels": True
    }

    pos = nx.circular_layout(G)
    nx.draw(G, pos, **options)
    plt.title("Transport Network Graph")
    plt.legend((f"nodes - {G.number_of_nodes()}", f"edges - {G.number_of_edges()}"))
    plt.show()
    
def param(G):
    num_nodes = G.number_of_nodes()  
    num_edges = G.number_of_edges()  
    num_degree = G.degree  

    print(f"{num_degree} - Ступінь вершин")
    print(f"{num_edges} - Кількість ребер")
    print(f"{num_nodes} - Кількість вершин")
    
def main():
    G = create_transport_graph()
    visualize_graph(G)
    param(G)

if __name__ == "__main__":
    main()
