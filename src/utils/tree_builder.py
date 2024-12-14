from ..models.node import Node


def create_tree_from_dict(tree_dict: dict) -> Node:
    def create_tree(dictionary, parent_name="root"):
        if not dictionary:
            return Node(parent_name, is_file=True)

        root = Node(parent_name, is_file=False)
        for key, value in dictionary.items():
            child = create_tree(value, key)
            root.add_child(child)
        return root

    return create_tree(tree_dict)