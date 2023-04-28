from nltk import Tree


def find_parent(tree: Tree, label: str) -> dict:
    dict_of_parents = {}
    for pos in tree.treepositions():
        if isinstance(tree[pos], Tree) and tree[pos].label() == label:
            if len([subtree for subtree in tree[pos] if subtree.label() == label]) > 1:
                dict_of_parents[pos] = tree[pos]

    return dict_of_parents
