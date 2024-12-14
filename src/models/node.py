from typing import List, Optional


class Node:
    def __init__(self, name: str, is_file: bool = False):
        self.name = name
        self.is_file = is_file
        self.children = []
        self.parent = None
        self.depth = 0
        self.path_to_root = []

    def add_child(self, child: 'Node'):
        child.parent = self
        child.depth = self.depth + 1
        child.update_path_to_root()
        self.children.append(child)

    def update_path_to_root(self):
        current = self
        path = []
        while current:
            path.append(current.name)
            current = current.parent
        self.path_to_root = list(reversed(path))

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        node_type = "📄" if self.is_file else "📁"
        return f"{node_type} {self.name}"
