import networkx as nx
import matplotlib.pyplot as plt

def draw_mininet_topology():
    # Create a graph
    G = nx.Graph()

    # Add switches as nodes
    switches = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
    for switch in switches:
        G.add_node(switch, label='Switch')

    # Add hosts and connect to switches
    host_switch_pairs = [
        ('h1', 's1'), ('h2', 's2'), ('h3', 's2'),
        ('h4', 's3'), ('h5', 's4'), ('h6', 's5'),
        ('h7', 's5'), ('h8', 's5'), ('h9', 's6'),
        ('h10', 's7'), ('h11', 's7'), ('h12', 's8')
    ]

    for host, switch in host_switch_pairs:
        G.add_node(host, label='Host')
        G.add_edge(host, switch)

    # Add connections between switches
    switch_connections = [
        ('s1', 's2'), ('s2', 's3'), ('s2', 's5'),
        ('s4', 's5'), ('s5', 's6'), ('s6', 's7'),
        ('s7', 's8')
    ]

    for src, dest in switch_connections:
        G.add_edge(src, dest)

    # Draw the network graph
    pos = nx.spring_layout(G)  # Positions for all nodes
    plt.figure(figsize=(8, 8))

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")

    # Draw edges
    nx.draw_networkx_edges(G, pos, width=2, edge_color="blue")

    # Labels for all nodes
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    # Display the graph
    plt.title("Mininet Topology Visualization")
    plt.axis("off")  # Turn off the axis
    plt.show()

if __name__ == "__main__":
    draw_mininet_topology()
