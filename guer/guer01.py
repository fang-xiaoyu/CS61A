#%%
def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(117, 1)
    1
    >>> paths(3, 3)
    6
    """
    if m == 1:
        return 1
    if n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
from doctest import run_docstring_examples
run_docstring_examples(paths, globals(), True)
# %%
def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if s1 == [] or s2 ==[]:
        return s1 + s2
    else:
        if s1[0] < s2[0]:
            return [s1[0]] + merge(s1[1:], s2)
        else:
            return [s2[0]] + merge(s1, s2[1:])
run_docstring_examples(merge, globals(), True)

# %%
def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.
    >>> mario_number(' P P ') # jump, jump
    1
    >>> mario_number(' P P  ') # jump, jump, step
    1
    >>> mario_number('  P P ') # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ') # Mario cannot jump two plants
    0
    >>> mario_number('    ') # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    if len(level) == 0:
        return 1
    if len(level) == 1:
        return 1
    if len(level) == 2:
        return 1
    if level[1] == ' ':
        if level[2] == ' ':
            return mario_number(level[1:]) + mario_number(level[2:])
        else:
            return mario_number(level[1:])
    else:
        if level[2] == ' ':
            return mario_number(level[2:])
        else:
            return 0
run_docstring_examples(mario_number, globals(), True)
# %%
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for num in range(1,n):
        if cond(num):
            print(num)
run_docstring_examples(keep_ints, globals(), True)
# %%
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def make(func):
        for num in range(1, n):
            if func(num):
                print(num)
    return make
run_docstring_examples(make_keeper, globals(), True)
# %%
