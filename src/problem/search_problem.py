from typing import List, Optional
from ..models.node import Node


class TreeSearchProblem:
    def __init__(self, root: Node, target_name: str):
        self.root = root
        self.target_name = target_name
        self.nodes_visited = 0

    def get_successors(self, node: Node) -> List[Node]:
        return node.children

    def is_goal(self, node: Node) -> bool:
        return node.name == self.target_name

    def path_cost(self, node: Node) -> int:
        return self.nodes_visited

    def heuristic(self, node: Node) -> int:
        return 0 if node.name == self.target_name else 1
