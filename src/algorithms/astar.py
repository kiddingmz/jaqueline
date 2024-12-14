from typing import Optional, Tuple, List
import heapq
from ..models.node import Node
from ..problem.search_problem import TreeSearchProblem


def astar_search(problem: TreeSearchProblem) -> Tuple[Optional[Node], List[Node]]:
    frontier = [(0, problem.root)]
    explored = set()
    visited = []
    g_score = {problem.root: 0}

    while frontier:
        _, current_node = heapq.heappop(frontier)
        visited.append(current_node)
        problem.nodes_visited += 1

        if problem.is_goal(current_node):
            return current_node, visited

        explored.add(current_node)

        for successor in problem.get_successors(current_node):
            if successor in explored:
                continue

            tentative_g = g_score[current_node] + 1

            if successor not in g_score or tentative_g < g_score[successor]:
                g_score[successor] = tentative_g
                f_score = tentative_g + problem.heuristic(successor)
                heapq.heappush(frontier, (f_score, successor))

    return None, visited