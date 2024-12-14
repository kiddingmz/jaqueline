from ..models.node import Node
from typing import List


def print_tree(node: Node, prefix: str = ""):
    print(f"{prefix}{node}")
    for child in node.children:
        print_tree(child, prefix + "    ")


def print_path_to_goal(node: Node, visited_nodes: List[Node] = None):
    if not node:
        print("Caminho não encontrado!")
        return

    path = []
    current = node
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    print("\n=== Caminho até o objetivo ===")
    print("Início -> Fim:", " -> ".join([n.name for n in path]))
    print("\nDetalhes do caminho:")
    for i, node in enumerate(path):
        prefix = "└── " if i == len(path) - 1 else "├── "
        node_type = "📄" if node.is_file else "📁"
        depth_info = f"(Profundidade: {node.depth})"
        print(f"{' ' * (i * 4)}{prefix}{node_type} {node.name} {depth_info}")

    if visited_nodes:
        print(f"\nNós visitados durante a busca: {len(visited_nodes)}")
        print("Ordem de visitação:")
        for i, node in enumerate(visited_nodes, 1):
            print(f"{i}. {node.name}")
