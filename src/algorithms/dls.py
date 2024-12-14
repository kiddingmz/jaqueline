from typing import Optional, Tuple, List
from ..models.node import Node
from ..problem.search_problem import TreeSearchProblem


def depth_limited_search(problem: TreeSearchProblem, limit: int) -> Tuple[Optional[Node], List[Node]]:
    def recursive_dls(node: Node, limit: int, visited: List[Node]) -> Optional[Node]:
        if limit < 0:
            return None

        visited.append(node)
        problem.nodes_visited += 1

        if problem.is_goal(node):
            return node

        if limit > 0:
            for successor in problem.get_successors(node):
                result = recursive_dls(successor, limit - 1, visited)
                if result:
                    return result

        return None

    visited_nodes = []
    result = recursive_dls(problem.root, limit, visited_nodes)
    return result, visited_nodes