from itertools import permutations
from nltk import Tree
from copy import deepcopy


def find_parent(tree: Tree, label: str) -> dict:
    dict_of_parents = {}
    for pos in tree.treepositions():
        if isinstance(tree[pos], Tree) and tree[pos].label() == label:
            if len([subtree for subtree in tree[pos] if subtree.label() == label]) > 1:
                dict_of_parents[pos] = tree[pos]

    return dict_of_parents


def create_subtrees_permutation(subtree: Tree, label: str) -> list:
    position_and_subtree = {}

    for subtree_pos in subtree.treepositions():
        if (
                isinstance(subtree[subtree_pos], Tree)
                and subtree[subtree_pos].label() == label
                and subtree[subtree_pos].height() == 3
        ):
            position_and_subtree[subtree_pos] = subtree[subtree_pos]

    possible_permutations = permutations(position_and_subtree.values())

    subtrees_permuted = []
    for perm in possible_permutations:

        new_tree = deepcopy(subtree)
        for child, pos in zip(perm, position_and_subtree.keys()):
            new_tree[pos] = child

        subtrees_permuted.append(new_tree)

    return subtrees_permuted
