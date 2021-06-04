#%%
LAB_SOURCE_FILE = "lab05.py"

""" Lab 05: Trees and Proj2 Prep """
#%%
def merge(lst1, lst2):
    """Merges two sorted lists.
    >>> merge([1], [2])
    [1, 2]
    >>> merge([2], [1])
    [1, 2]
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if not lst1 or not lst2:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

from doctest import run_docstring_examples
run_docstring_examples(merge, globals(), True)
#%%
def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    if w1 == '' and w2 != '':
        return w2
    elif w1 == '' and w2 == '':
        return ''
    elif w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    else:
        return w2[0] + add_chars(w1, w2[1:])
run_docstring_examples(add_chars, globals(), True)
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
#%%
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
        lst = []
        for element in branches(t):
            lst += [acorn_finder(element)]
        if any(lst):
            return True
        else:
            return False
''' 
sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
print(label(sproul))
print(branches(sproul))
print(branches(sproul)[0])
print(label(branches(sproul)[1]))
print(branches(branches(sproul)[0]))
print(label(branches(branches(sproul)[0])))
print(is_tree(['tree']))
print(is_tree(['']))
print(is_tree([]))
'''
run_docstring_examples(acorn_finder, globals(), True)
# %%


""" Optional questions for Lab 05 """
#%%
from lab05 import *
#%%
# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [] 
        table[prev] += [word]
        prev = word
    return table
'''
table[prev] = []
"*** YOUR CODE HERE ***"
for i in range(len(tokens)):
if tokens[i] == prev:
if i != len(tokens) - 1:
table[prev] += [tokens[i + 1]]
else:
table[prev] += [tokens[0]]
else:
for i in range(len(tokens)):
if tokens[i] == prev and tokens[i + 1] not in table[prev] and i != len(tokens) - 1:
table[prev] += [tokens[i]]
'''
from doctest import run_docstring_examples
run_docstring_examples(build_successors_table, globals(), True)
#%%
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result = result + word + ' '
        word = random.choice(table[word])
    return result.strip() + word

run_docstring_examples(construct_sent, globals(), True)
#%%
def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def sent(word):
    return construct_sent(word, table)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
#%%
random_sent()
random_sent()
random_sent()
random_sent()
random_sent()
random_sent()
#%%
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
      for val in vals:
        t += [[val]]
    else:
      for branch in branches(t):
        branch = sprout_leaves(branch, vals)
      return t
    '''
    if is_leaf(t):
      return tree(label(t),[tree(x) for x in vals])
    else:
      lst=[]
      for b in branches(t):
        lst+=[sprout_leaves(b,vals)]
      return tree(label(t),lst)
      '''
run_docstring_examples(sprout_leaves, globals(), True)
#%%
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
      return tree(label(t1) + label(t2), branches(t2))
    elif is_leaf(t2):
      return tree(label(t1) + label(t2), branches(t1))
    else:
      branch = []
      sb1 = branches(t1)
      sb2 = branches(t2)
      l1 = len(sb1)
      l2 = len(sb2)
      if l1 > l2:
        sb2 += [[0]] * (l1 - l2)
      elif l1 < l2:
        sb1 += [[0]] * (l2 - l1)

      for b1, b2 in zip(sb1, sb2):
        branch += [add_trees(b1,b2)]
      return tree(label(t1) + label(t2), branch)
run_docstring_examples(add_trees, globals(), True)

