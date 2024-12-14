from src.models.node import Node
from src.problem.search_problem import TreeSearchProblem
from src.algorithms.dls import depth_limited_search
from src.algorithms.astar import astar_search
from src.utils.tree_builder import create_tree_from_dict
from src.utils.visualizer import print_tree, print_path_to_goal


def main():
    # Criar árvore de exemplo
    tree_dict = {
        "Documentos": {
            "Trabalho": {
                "relatorio.txt": {},
                "dados.xlsx": {}
            },
            "Pessoal": {
                "fotos": {
                    "ferias.jpg": {},
                    "familia.jpg": {}
                },
                "notas.txt": {}
            }
        }
    }

    root = create_tree_from_dict(tree_dict)

    print("\nEstrutura da árvore:")
    print_tree(root)

    # Testar busca
    target = "familia.jp"
    problem = TreeSearchProblem(root, target)

    print(f"\nBuscando por: {target}")

    # DLS
    found_node, visited = depth_limited_search(problem, limit=4)
    if found_node:
        print("\nResultado da Busca em Profundidade Limitada:")
        print_path_to_goal(found_node, visited)

    # A*
    problem.nodes_visited = 0  # Reset contador
    found_node, visited = astar_search(problem)
    if found_node:
        print("\nResultado da Busca A*:")
        print_path_to_goal(found_node, visited)


if __name__ == "__main__":
    main()
