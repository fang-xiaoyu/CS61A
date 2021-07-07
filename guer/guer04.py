#%%
class Link:
    """A linked list.
    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.
        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.
        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
from doctest import run_docstring_examples
#%%
class Cat():
    noise = 'meow'
    def __init__(self, name):
        self.name = name
        self.hungry = True
    def meow(self):
        if self.hungry:
            print(self.noise + ', ' + self.name + ' is hungry')
        else:
            print(self.noise + ', my name is ' + self.name)
    def eat(self):
        print(self.noise)
        self.hungry = False

class Kitten(Cat):
    noise = "i'm baby"
    def __init__(self, name, parent):
        Cat.__init__(self, name)
        self.parent_name = parent.name
    def meow(self):
        Cat.meow(self)
        print('I want mama ' + self.parent_name)
# %%
cat = Cat('Tuna')
kitten = Kitten('Fish', cat)
cat.meow()
# %%
kitten.meow()
# %%
cat.eat()
# %%
cat.meow()
# %%
kitten.eat()
# %%
kitten.meow()
# %%
def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    Tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """
    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches[:]:
            if not fn(b.label):
                t.branches.remove(b)
            else:
                filter_tree(b, fn)       
run_docstring_examples(filter_tree, globals(), True)
# %%
def nth_level_tree_map(fn, t, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]),Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]), Tree(2, [Tree(7), Tree(5)])])
    """
    def helper(t, level=0):
        if not level % n:
            t.label = fn(t.label)
        if not t.is_leaf():
            for b in t.branches[:]:
                helper(b, level + 1)
    helper(t)          
run_docstring_examples(nth_level_tree_map, globals(), True)
# %%
def has_cycle_two_pointers(link):
    """Return whether link contains a cycle.
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_two_pointers(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_two_pointers(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle_two_pointers(u)
    False
    """
    '''
    first_pointer, second_pointer = link, link.rest
    while second_pointer:
        if second_pointer is first_pointer:
            return True
        else:
            second_pointer = second_pointer.rest
    return False
    '''
    first_pointer, second_pointer = link, link.rest
    while first_pointer.rest and second_pointer.rest and second_pointer.rest.rest:
        if second_pointer is first_pointer:
            return True
        else:
            first_pointer = first_pointer.rest
            second_pointer = second_pointer.rest.rest
    return False
run_docstring_examples(has_cycle_two_pointers, globals(), True)
# %%
def has_cycle_track(link):
    """Return whether link contains a cycle.
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_track(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_track(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle_track(u)
    False
    """
    seen = []
    while link.rest:
        if link.rest in seen:
            return True
        else:
            seen.append(link.rest)
            link = link.rest
    return False
run_docstring_examples(has_cycle_track, globals(), True)
# %%
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if not sub_link:
        return True
    if not link:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest, sub_link)
run_docstring_examples(seq_in_link, globals(), True)
