from copy import deepcopy
from itertools import permutations, product

from nltk import Tree


def find_parent(tree: Tree, label: str) -> dict:
    """
    Function finds parents with certain label which has children to be permuted
    """
    dict_of_parents = {}
    for pos in tree.treepositions():
        if isinstance(tree[pos], Tree) and tree[pos].label() == label:
            if len(
                    [sub for sub in tree[pos] if sub.label() == label]
            ) > 1:
                dict_of_parents[pos] = tree[pos]

    return dict_of_parents


def create_subtree_permutation(subtree: Tree, label: str) -> list:
    """
    Function to create permutation of children with certain label for subtree
    """
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


def subtrees_product_permutations(tree: Tree, label: str):
    """
    Function to create product of all subtrees permutations
    """
    parent_trees = find_parent(tree, label)
    children_permutations = [
        create_subtree_permutation(subtree, label)
        for subtree
        in parent_trees.values()
    ]
    return list(product(*children_permutations))


def build_new_trees(
        tree: Tree,
        label: str,
        limit: int
) -> list:
    """
    Function to build new trees with all permutations based on original tree
    """
    new_final_trees = []
    parent_trees = find_parent(tree, label).keys()
    product_permutations = subtrees_product_permutations(tree, label)

    for subtree_permuted in product_permutations:
        new_tree = deepcopy(tree)
        for pos, sub in zip(parent_trees, subtree_permuted):
            new_tree[pos] = sub
        new_final_trees.append(new_tree)

    return new_final_trees[:limit]


def build_paraphrases(tree: Tree, label: str, limit: int) -> dict:
    """
    Function to build dict of paraphrases using given tree and label
    """
    new_trees = build_new_trees(tree, label, limit)

    trees_to_str = [" ".join(str(tree).split()) for tree in new_trees]
    tree_dict = {"paraphrases": [{"tree": tree} for tree in trees_to_str]}
    return tree_dict
