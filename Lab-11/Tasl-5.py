class Graph:
    """
    Graph implementation using an adjacency list.
    Supports adding edges and performing BFS and DFS traversals.
    """
    def __init__(self):
        # Initialize the adjacency list as a dictionary
        self.adj_list = {}

    def add_edge(self, u, v):
        """
        Adds an undirected edge between node u and node v.
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        # Add both edges since the graph is undirected
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        """
        Breadth-First Search traversal from the starting node.
        Prints the order of traversal with explanatory comments.
        """
        from collections import deque

        visited = set()                  # Set to keep track of visited nodes
        queue = deque([start])           # Use a queue for BFS

        print(f"Starting BFS from node {start}")
        while queue:
            node = queue.popleft()       # Dequeue a node for exploration
            if node not in visited:
                print(f"Visiting: {node}")
                visited.add(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        print(f"  Queueing neighbor {neighbor} of {node}")
                        queue.append(neighbor)
        print("BFS traversal complete.")

    def dfs(self, start):
        """
        Depth-First Search traversal from the starting node.
        Prints the order of traversal with explanatory comments.
        """
        visited = set()

        print(f"Starting DFS from node {start}")
        def dfs_recursive(node):
            print(f"Visiting: {node}")
            visited.add(node)
            # Explore each neighbor recursively if not visited
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    print(f"  Going deeper to neighbor {neighbor} of {node}")
                    dfs_recursive(neighbor)
        dfs_recursive(start)
        print("DFS traversal complete.")

# Example usage:
if __name__ == "__main__":
    g = Graph()
    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("Adjacency List Representation:")
    for node, neighbors in g.adj_list.items():
        print(f"{node}: {neighbors}")

    print("\nBFS Traversal Example:")
    g.bfs(0)

    print("\nDFS Traversal Example:")
    g.dfs(0)
