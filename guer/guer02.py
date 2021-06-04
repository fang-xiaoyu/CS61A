#%%
# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.
    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
# %%
def map_mut(f, L):
    """
    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    for i in range(len(L)):
        L[i] = f(L[i])
from doctest import run_docstring_examples
run_docstring_examples(map_mut, globals(), True)
# %%
def is_min_heap(t):
    """
    >>> t1 = tree(1,[tree(5,[tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)])
    >>> is_min_heap(t1)
    True
    >>> t2 = tree(1,[tree(5,[tree(7)]),tree(3,[tree(9),tree(2)]),tree(6)])
    >>> is_min_heap(t2)
    False
    """
    '''
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True
    '''
    if is_leaf(t):
        return True
    else:
        lst = []
        for b in branches(t):
            if label(t) <= label(b) and is_min_heap(b):
                lst += []
            else:
                lst += [1]
        if 1 in lst:
            return False
        else:
            return True
run_docstring_examples(is_min_heap, globals(), True)
# %%
def largest_product_path(t):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    if not t:
        return 0
    if is_leaf(t):
        return label(t)
    else:
        lst = []
        for b in branches(t):
            lst.append(label(t) * largest_product_path(b))
        return max(lst)
run_docstring_examples(largest_product_path, globals(), True)
# %%
def max_tree(t):
    """
    >>> max_tree(tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))
    [9, [7, [7]], [9, [9], [4]], [6]]
    """
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max(label(b) for b in new_branches)
        return tree(new_label, new_branches)         
run_docstring_examples(max_tree, globals(), True)
# %%
def level_order(t):
    """
    >>> t1 = tree(1, [tree(5, [tree(7)]),tree(3,[tree(9, [tree(8)]),tree(4)]),tree(6)])
    >>> level_order(t1)
    [1, 5, 3, 6, 7, 9, 4, 8]
    """
    '''
    if is_leaf(t):
        return [label(t)]
    else:
        lst = [label(t)]
        for b in branches(t):
            lst += level_order(b)
        return lst
    '''
    current_level, next_level = [label(t)], [t]
    while next_level:
        find_next = []
        for b in next_level:
            find_next.extend(branches(b))
        next_level = find_next
        current_level.extend(label(t) for t in next_level)
    return current_level
run_docstring_examples(level_order, globals(), True)
# %%
def all_path(t):
    """
    >>> t1 = tree(3, [tree(7), tree(8), tree(4)])
    >>> all_path(t1)
    [[3, 7], [3, 8], [3, 4]]
    >>> t2 = tree(3, [tree(7, [tree(1), tree(2)]), tree(8), tree(4, [tree(5, [tree(6)])])])
    >>> all_path(t2)
    [[3, 7, 1], [3, 7, 2], [3, 8], [3, 4, 5, 6]]
    """
    if is_leaf(t):
        return [t]
    else:
        lst = []
        for b in branches(t):
            for p in all_path(b):
                lst += [[label(t)] + p]
        return lst
run_docstring_examples(all_path, globals(), True)
# %%
t1 = tree(3, [tree(7, [tree(1), tree(2)]), tree(8), tree(4, [tree(5, [tree(6)])])])
print(t1)
# %%
