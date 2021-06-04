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
def count_codes(t):
    """
    >>> t = tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])])
    >>> count_codes(t)
    9
    """
    if is_leaf(t):
        return 1
    else:
        total = 0
        for b in branches(t):
            total += count_codes(b)
        return 1 + total
from doctest import run_docstring_examples
run_docstring_examples(count_codes, globals(), True)
# %%
def collect_leaves(t):
    """
    >>> t = tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])])
    >>> collect_leaves(t)
    [2, 3, 1, 1, 1]
    >>> t2 = tree('D', [tree('B', [tree('A'), tree('C')]), tree('F', [tree('E'), tree('H', [tree('G'), tree('I')])])])
    >>> collect_leaves(t2)
    ['A', 'C', 'E', 'G', 'I']
    """
    if is_leaf(t):
        return [label(t)]
    '''
    lst = []
    for b in branches(t):
        lst += collect_leaves(b)
    '''
    lst = [collect_leaves(b) for b in branches(t)]
    return sum(lst, [])
run_docstring_examples(collect_leaves, globals(), True)
# %%
def print_call(name, f):
    def new_f(t):
        print('Name: ', name)
        print('Inputted tree: ')
        print_tree(t)
        input()
        ret = f(t)
        print('Returned tree: ', ret)
        return ret
    return new_f
t = tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])])
collect_leaves = print_call('collect_leaves', collect_leaves)
collect_leaves(t)

# %%
def square_tree(t):
    """Return a tree with the square of every element in t.
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                         [tree(3),
    ...                          tree(4)]),
    ...                  tree(5,
    ...                         [tree(6,
    ...                                 [tree(7)]),
    ...                          tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        lst = []
        for b in branches(t):
            lst += [square_tree(b)]
        return tree(label(t) ** 2, lst)
from doctest import run_docstring_examples
run_docstring_examples(square_tree, globals(), True)
# %%
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    >>> t = tree(1, [tree('acorn',[tree('not acorn')])])
    >>> acorn_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    if label(t) == 'acorn':
        return True
    else:
        lst =[]
        for b in branches(t):
            lst += [acorn_finder(b)]
        if any(lst):
            return True
        else:
            return False
run_docstring_examples(acorn_finder, globals(), True)
# %%
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(el) for el in vals])
    else:
        lst = []
        for b in branches(t):
            lst += [sprout_leaves(b, vals)]
        return tree(label(t), lst)
run_docstring_examples(sprout_leaves, globals(), True)
# %%
t1 = tree(2, [tree(1)])
t2 = tree(3, [tree(4), tree(5)])
br1 = branches(t1)
br2 = branches(t2)
if len(br1) < len(br2):
    br1 += [[0]] * (len(br2) - len(br1))
print(br1)
print(br2)
for b1,b2 in zip(branches(t1), branches(t2)):
    print(b1)
    print(b2)
# %%
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t1):
        if is_leaf(t2):
            return tree(label(t1) + label(t2))
        else:
            return tree(label(t1) + label(t2), branches(t2))
    else:
        if is_leaf(t2):
            return tree(label(t1) + label(t2), branches(t1))
        else:
            lst = []
            br1, br2 = branches(t1), branches(t2)
            len1, len2 = len(br1), len(br2)
            if len1 < len2:
                br1 += [[0]] * (len2 -len1)
            elif len2 < len1:
                br2 += [[0]] * (len1 -len2)
            for b1, b2 in zip(br1, br2):
                lst += [add_trees(b1, b2)]
            return tree(label(t1) + label(t2), lst)
run_docstring_examples(add_trees, globals(), True)
# %%
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5,), tree(2, [tree(1, [tree(1)])])])
    >>> height(t)
    3
    >>> y = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> height(y)
    2
    """
    if is_leaf(t):
        return 0
    else:
        lst = []
        for b in branches(t):
            lst += [height(b)]
        return 1 + max(lst)
run_docstring_examples(height, globals(), True) 
# %%
def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(11)]), tree(10)])
    >>> tree_max(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        lst = []
        for b in branches(t):
            lst += [tree_max(b)]
        return max(lst)
run_docstring_examples(tree_max, globals(), True) 
# %%
def find_path(t, x):
    """
    >>> tt = tree(1)
    >>> find_path(tt, 1)
    [1]
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(t) and label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if type(path) == list:
            return [label(t)] + path
run_docstring_examples(find_path, globals(), True) 
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
    if is_leaf(t):
        return True
    else:
        lst = []
        for b in branches(t):
            if label(b) > label(t):
                lst += [is_min_heap(b)]
            else:
                lst += [False]
        if all(lst):
            return True
        else:
            return False
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
            lst += [largest_product_path(b)]
        return label(t) * max(lst)        
run_docstring_examples(largest_product_path, globals(), True) 
# %%
def contains(t, e):
    """
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> contains(t, 7)
    True
    >>> contains(t, 77)
    False
    """
    if is_leaf(t) and label(t) != e:
        return False
    if e == label(t):
        return True
    lst = []
    for b in branches(t):
        return contains(b, e)
run_docstring_examples(contains, globals(), True) 
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
        new_label = max(label(bb) for bb in new_branches)
        return tree(new_label, new_branches)
run_docstring_examples(max_tree, globals(), True) 
# %%
def level_order(t):
    """
    >>> t1 = tree(1, [tree(5, [tree(7)]),tree(3,[tree(9, [tree(8)]),tree(4)]),tree(6)])
    >>> level_order(t1)
    [1, 5, 3, 6, 7, 9, 4, 8]
    """
    current_level, next_level = [label(t)], [t]
    while next_level:
        find_level = []
        for tt in next_level:
            find_level += branches(tt)
        next_level = find_level
        current_level += [label(ttt) for ttt in next_level]
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
t1 = tree(3, [tree(7), tree(8), tree(4)])
print(t1)
# %%
