from copy import deepcopy
from itertools import permutations

from nltk import Tree


def find_parent(tree: Tree, label: str) -> dict:
    dict_of_parents = {}
    for pos in tree.treepositions():
        if isinstance(tree[pos], Tree) and tree[pos].label() == label:
            if len(
                    [sub for sub in tree[pos] if sub.label() == label]
            ) > 1:
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


def build_new_trees(
        subtrees_permuted: list[list[Tree]],
        tree: Tree,
        limit: int
) -> list:
    new_final_trees = []
    parent_trees = find_parent(tree, "NP").keys()
    for pos, subtree_permuted in zip(parent_trees, subtrees_permuted):
        for subtree in subtree_permuted:
            new_tree = deepcopy(tree)
            new_tree[pos] = subtree
            new_final_trees.append(new_tree)

    return new_final_trees[:limit]


def build_paraphrases(tree: Tree, label: str, limit: int) -> dict:
    parent_trees = find_parent(tree, label)
    children_permutations = [
        create_subtrees_permutation(subtree, label)
        for subtree
        in parent_trees.values()
    ]
    new_trees = build_new_trees(children_permutations, tree, limit)

    trees_to_str = [" ".join(str(tree).split()) for tree in new_trees]
    tree_dict = {"paraphrases": [{"tree": tree} for tree in trees_to_str]}
    return tree_dict
