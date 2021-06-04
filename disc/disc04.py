#%%
# == : 用来比较value是否相等
# is : 用来比较identity是否相等
# 只有数值型和字符串型的情况下，a is b才为True，
# 当a和b是tuple，list，dict或set型时，a is b为False。
#########
# Trees #
#########

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

#%%
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5,), tree(2, [tree(1)])])
    >>> height(t)
    2
    >>> y = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> height(y)
    2
    """
    if is_leaf(t):
        return 0
    else:
        height_b = 0
        for branch in branches(t):
            height_b = max(height(branch) + 1, height_b)
        return height_b

from doctest import run_docstring_examples
run_docstring_examples(height, globals(), True)
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
        for branch in branches(t):
            lst += [square_tree(branch)]
        return tree(label(t) ** 2, lst)
run_docstring_examples(square_tree, globals(), True)
# %%
def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    if is_leaf(t):
        return label(t)
    else:
        max_b = 0
        for branch in branches(t):
            max_b = max(max_b, tree_max(branch))
        return max_b
run_docstring_examples(tree_max, globals(), True)
# %%
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(t) and label(t) == x:
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch, x)
        if type(path) == list:
            return [label(t)] + path

run_docstring_examples(find_path, globals(), True)
# %%
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 2, 2]
    """
    def add_el():
        lst.append(el)
        return add_this_many(x - 1, el, lst)
    if x > 0:    
        return add_el()    
    else:
        return None
run_docstring_examples(add_this_many, globals(), True)
# %%
def add_this_many_2(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 2, 2]
    """
    t=lst.count(x)
    while t>0:
        lst.append(el)
        t-=1
run_docstring_examples(add_this_many_2, globals(), True)
# %%
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    dic = {}
    for el in s:
        if fn(el) not in dic:
            dic[fn(el)] = [el]
        else:
            dic[fn(el)] += [el]
    return dic 
run_docstring_examples(group_by, globals(), True)
