#%%
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_ever = 0
    def find_max_ever(lst):
        nonlocal max_ever
        lst.append(max_ever)
        max_ever = max(lst)
        return max_ever
    return find_max_ever
from doctest import run_docstring_examples
run_docstring_examples(make_max_finder, globals(), True)
# %%
x = 5
def f(x):
    def g(s):
        def h(h):
            nonlocal x
            x = x + h
            print(x)
            return x
        nonlocal x
        x = x + x
        return h
    print(x)
    return g

t = f(7)(8)(9)

# %%
def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x
run_docstring_examples(generate_constant, globals(), True)
# %%
def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for el in seq:
        if el == trap:
            while True:
                yield trap
        else:
            yield el
run_docstring_examples(black_hole, globals(), True)
#%%
def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4
    """
    while True:
        '''
        lst += lst
        for el in lst:
            yield el
        '''
        for i in range(len(lst)):
            yield lst[i]
run_docstring_examples(gen_inf, globals(), True)
# %%
def naturals():
    i = 1
    while True:
        yield i
        i += 1

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for el in iterable:
        if fn(el):
            yield el
run_docstring_examples(filter, globals(), True)
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
def tree_sequence(t):
    """
    >>> t = tree(1, [tree(2, [tree(5)]), tree(3, [tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    def build_lst():
        if is_leaf(t):
            return [label(t)]
        else:
            lst = []
            for b in branches(t):
                lst += tree_sequence(b)
            return [label(t)] + lst
    lst = build_lst()
    for el in lst:
        yield el
run_docstring_examples(tree_sequence, globals(), True)
# %%
def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ...     print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    lst = []
    def digit_get():
        nonlocal n, lst
        if n == 0:
            return sum(lst)
        else:
            res = n % 10
            lst.append(res)
            n = n // 10
            return res          
    return digit_get
run_docstring_examples(make_digit_getter, globals(), True)
# %%
